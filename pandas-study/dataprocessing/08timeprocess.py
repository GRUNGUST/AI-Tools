import pandas as pd
import datetime
import numpy as np
from matplotlib import pyplot as plt

## 解析时间
# df = pd.DataFrame({
#     "time": ["2022/03/12", "2022/03/13", "2022/03/14"],
#     "value": [1, 2, 3]
# })

# print(df)
# print(pd.to_datetime(df["time"]))
# print(pd.to_datetime(
#     ["2022/03/12", "2022.03.13", "14/03/2022"]
# ))
# print(pd.to_datetime(
#     [
#         "1@21@2022%%11|11|32",
#         "12@01@2022%%44|02|2",
#         "4@01@2022%%14|22|2"
#     ],
#     format="%m@%d@%Y%%%%%S|%H|%M"
# ))

## 自建时间序列
# start = datetime.datetime(2022, 3, 12)
# end = datetime.datetime(2022, 3, 18)
#
# index = pd.date_range(start, end)
# print(index)
# print(
#     "\n\npd.date_range()\n",
#     pd.date_range(start, end, freq="48h")
# )

# 切割时间为5份
# print(
#     "\n\npd.date_range(start, end, periods=5)\n",
#     pd.date_range(start, end, periods=5)
# )


start = datetime.datetime(2022, 3, 1)
end = datetime.datetime(2022, 5, 3)

rng = pd.date_range(start, end)
ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print(rng)
# (ts.index)
# ts.plot()
# ts[1:8].plot()

# t1 = datetime.datetime(2022, 3, 12)
# t2 = datetime.datetime(2022, 3, 18)
# ts[t1: t2].plot()

# ts["2022-03-12": "2022-03-18"].plot()
# plt.show()

## 时间运算
# rng = pd.date_range("2022-01-01", "2022-01-07")
# 加一周
# print(rng + pd.Timedelta(weeks=1))
# print(rng + 2 * pd.Timedelta(days=3))

rng = pd.date_range("2022-01-08", "2022-01-11")
# print(rng.dayofyear)
# print(rng.dayofweek)

print(rng.strftime("%m/%d/%Y"))
