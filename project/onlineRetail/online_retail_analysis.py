import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import ticker

import project.common as com

# print(com.check_encoding('data/new_online_retail.csv'))
retails = pd.read_csv('data/new_online_retail.csv', encoding="latin1")

## 匿名用户交易分布
# anonymous_retails = retails[retails['Anonymous'] == 1]
# print(anonymous_retails.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False))

## 热门商品排行榜
# print(retails.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10))

## 按时间分析销售趋势

retails['InvoiceDate'] = pd.to_datetime(retails['InvoiceDate'])
# 按日期排序
retails = retails.sort_values("InvoiceDate")

ts_retails = retails.set_index("InvoiceDate")

# 按日聚合
# daily_sales = ts_retails.resample('D')['TotalPrice'].sum().fillna(0)

# 按周聚合
# weekly_sales = ts_retails.resample('W-MON')['TotalPrice'].sum()
# print(weekly_sales)

monthly_sales = ts_retails.resample('ME')['TotalPrice'].sum()

plt.figure(figsize=(14, 7))

plt.plot(monthly_sales.index, monthly_sales.values, marker="o", linestyle="-", color="royalblue")

# 添加标签和格式
plt.title("Monthly Sales Trend", fontsize=15)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total Sales (USD)", fontsize=12)
plt.grid(True, alpha=0.3)

# 配置 x 轴
ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
# ax.set_xlim([monthly_sales.index.min(), monthly_sales.index.max()])

ax.yaxis.set_major_formatter(ticker.FuncFormatter(com.science_format_func))
plt.xticks(rotation=45)

plt.show()
