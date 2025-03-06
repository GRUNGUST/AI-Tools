import pandas as pd
import numpy as np

# data = np.array([
#     [1.39, 1.77, None],
#     [0.34, 1.91, -0.05],
#     [0.34, 1.47, 1.22],
#     [None, 0.27, -0.61]
# ])

# df = pd.DataFrame(data, index=["r0", "r1", "r2", "r3"], columns=["c0", "c1", "c2"])
# count 有效数据个数，unique 独特的数据，top 出现最多的数据，freq top数据出现的频率
# print(df.describe())

# df1 = pd.DataFrame(np.random.random((4,3)), columns=["c0", "c1", "c2"])
# print(df1)
# print("\ndescribe:\n", df1.describe())

## 均值中位数
# print(df.mean())
# 按行计算均值
# print(df.mean(axis=1))

# s = pd.Series([1000, 2000, 4000, 100000])
# print("mean():", s.mean())  # 拉高平均收入，拉高仇恨
# print("median():", s.median())  # 比较合理

## 累加累乘
# df = pd.DataFrame(np.arange(12).reshape((4, 3)), columns=["c0", "c1", "c2"])
# print(df)
# print("sum():\n", df.sum())
# print("\nsum(axis=0):\n", df.sum(axis=0))
# print("\nsum(axis=1):\n", df.sum(axis=1))

# 累乘
# print("prod():\n", df.prod())
# print("\nprod(axis=0):\n", df.prod(axis=0))
# print("\nprod(axis=1):\n", df.prod(axis=1))

# 最大最小
# print("max():\n", df.max())
# print("min():\n", df.min())

# print(df.max().max())
# dataframe -> numpy -> list
# print(df.values.ravel().max())

## 处理空值
df = pd.DataFrame([[1, 2, 3, 0],
                   [3, 4, None, 1],
                   [None, None, None, None],
                   [None, 3, None, 4]],
                  columns=list("ABCD"))

# print(df)
# print("\nisnull():\n", df.isnull())  # True 就是空
# print("\nnotnull()\n", df.notnull())  # False 为空

# drop 掉 空值
# print("默认：\n", df.dropna())
# print("\naxis=1:\n", df.dropna(axis=1))

df1 = pd.DataFrame([[None, None, None], [1, None, 3]])
# print(df1.dropna(how="all"))  # how 默认为 "any"

# 填充空值
# print(df.fillna(111))
# 按列填充值
# values = {"A": 0, "B": 1, "C": 2, "D": 3}
# print(df.fillna(value=values))

# df2 = pd.DataFrame(np.arange(16).reshape(4, 4), columns=list("ABCD"))
# print(df2)
# print(df.fillna(df2))


## 获取索引
df = pd.DataFrame([[1, 2, 3, 0],
                   [3, 4, None, 1],
                   [3, 5, 2, 1],
                   [3, 2, 2, 3]],
                  columns=list("ABCD"))
print(df)
print("\nidxmax():\n", df.idxmax())
print("\nidxmax(skipna=False):\n", df.idxmax(skipna=False))
print("\nidxmin():\n", df.idxmin())
