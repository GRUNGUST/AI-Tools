import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/day_wise.csv")

# print(df.head())

## 获取 2020 年 2 月 3 日的所有数据
# print(df[df["Date"] == "2020-02-03"])

## 2020 年 1 月 24 日之前的累积确诊病例有多少个？
# confirmed0124 = df.loc[df["Date"] == "2020-01-24", "Confirmed"]
# print(confirmed0124.values)

## 2020 年 7 月 23 日的新增死亡数是多少？
# deaths0723 = df.loc[df["Date"] == "2020-07-23", "New deaths"]
# print(deaths0723.values)

## 从 1 月 25 日到 7 月 22 日，一共增长了多少确诊病例？
# date = pd.to_datetime(df["Date"])
# date_range = (date >= "2020-01-25") & (date <= "2020-07-22")
# overall = df.loc[date_range, "New cases"].sum()
# print(overall)
#
# confirmed0125 = df.loc[df["Date"] == "2020-01-25", "Confirmed"].values
# confirmed0722 = df.loc[df["Date"] == "2020-07-22", "Confirmed"].values
# print(confirmed0722 - confirmed0125)

# 分析对不上的原因
# confirmed = df["Confirmed"]
# new_cases = df["New cases"]
# idx_0722 = df.loc[df["Date"] == "2020-07-22"].index.item()
# idx_0125 = df.loc[df["Date"] == "2020-01-25"].index.item()
#
# for i in range(idx_0125, idx_0722):
#     diff = new_cases.iloc[i] - (confirmed.iloc[i] - confirmed.iloc[i - 1])
#     if diff != 0:
#         print("date index:", i, ";差异：", diff)


## 每天新增确诊数和新恢复数的比例？平均比例，标准差各是多少？
# ratio = df["New cases"] / df["New recovered"]
# print("比例样本：", ratio[:5])

# not_zero_mask = df["New recovered"] != 0
# ratio = df.loc[not_zero_mask, "New cases"] / df.loc[not_zero_mask, "New recovered"]
# print("比例样本：", ratio[:5])
#
# ratio_mean = ratio.mean()
# ratio_std = ratio.std()
# print("平均比例：", ratio_mean, "；标准差：", ratio_std)

#df["New cases"].plot()
#print(df.loc[50, "Date"])
df["Deaths / 100 Cases"].plot()
plt.show()
