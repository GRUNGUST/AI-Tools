import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import common as com

# encoding = com.check_encoding('data/OnlineRetail.csv')
retails = pd.read_csv('data/OnlineRetail.csv', encoding="latin1")
# print(retails.info())
# print(retails.size)


## 数据清洗
# 计算缺失比例
miss_ratio = retails['CustomerID'].isnull().mean()
# print(miss_ratio)

# 删除缺失行（适用于缺失比例较低或分析需要完整客户信息）
# new_retails = retails.dropna(subset=['CustomerID']).copy()

# 保留匿名交易（用于分析非注册客户行为）
# retails['CustomerID'] = retails['CustomerID'].fillna("Anonymous")

# 新创建一列记录非法用户
retails["Anonymous"] = retails['CustomerID'].isnull().astype(int)

# 删除cancel的订单（开头是C）
new_retails = retails[~retails['InvoiceNo'].astype(str).str.startswith("C")]
# print(new_retails.info())

# 删除负数 Quantity  和负数 UnitPrice 的数据
no_quantity_index = new_retails[new_retails['Quantity'] <= 0].index
new_retails = new_retails.drop(no_quantity_index)
no_unitprice_index = new_retails[new_retails['UnitPrice'] <= 0].index
new_retails = new_retails.drop(no_unitprice_index)

## 处理重复值
# 完全重复项
# print(new_retails.duplicated().sum())
# print(new_retails[new_retails.duplicated(keep=False)].sort_values(by=["InvoiceNo", "StockCode"]).head(6))

subset_cols = ["InvoiceNo", "StockCode"]
# print(f'业务关键列重复数:{new_retails.duplicated(subset=subset_cols).sum()}')

new_retails = new_retails.drop_duplicates(subset=subset_cols, keep="first")

## 规范数据类型
# 转换 CustomerID 为整数
new_retails['CustomerID'] = new_retails['CustomerID'].astype(float).astype("Int64")

# 转换正常日期
new_retails['InvoiceDate'] = pd.to_datetime(retails['InvoiceDate'])

# 提取日期特征
# new_retails['InvoiceYearMonth'] = new_retails['InvoiceDate'].dt.to_period("M")

## 处理异常值
# IQR 过滤数量异常
Q1 = new_retails["Quantity"].quantile(0.25)
Q3 = new_retails["Quantity"].quantile(0.75)
IQR = Q3 - Q1
new_retails = new_retails[
    ~((new_retails["Quantity"] < (Q1 - 1.5 * IQR)) | (new_retails["Quantity"] > (Q3 + 1.5 * IQR)))]
# print(new_retails.describe()[["Quantity", "UnitPrice"]])

# 计算每笔订单的总金额
new_retails["TotalPrice"] = new_retails["Quantity"] * new_retails["UnitPrice"]
new_retails = new_retails[(new_retails["TotalPrice"] < 10_000) & (new_retails["TotalPrice"] > 0.01)]

# 检查异常商品描述
#print(new_retails["Description"].value_counts().head(10))

new_retails["Description"] = new_retails["Description"].str.strip().str.lower()

new_retails.to_csv("data/new_online_retail.csv", index=False)
