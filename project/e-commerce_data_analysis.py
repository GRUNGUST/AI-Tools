import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## 加载数据
df = pd.read_csv('data/Superstore.csv', encoding='latin1')
# print(df.head())  # 查看前5行
#print(df.info())  # 检查数据类型和缺失值

## 数据清洗
# 查看哪一列会有空值
# print(df.isna().any())

# 转换日期格式
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# 检查异常值（负利润）
negative_profit = df[df['Profit'] < 0]
print("负利润订单占比: ", len(negative_profit)/len(df))
