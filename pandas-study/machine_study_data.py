import pandas as pd
from matplotlib import pyplot as plt

path = "data/iris.csv"
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df = pd.read_csv("data/iris.csv", names=columns)

# NaN处理
# 查找出哪列有数据空值
# print(df.isna().any())
# print(df.loc[pd.isna(df["petal_width"])])
# 数据量少时可以直接丢掉空值
df1 = df.dropna(axis=0, how="any")
# print(df1.isna().any())


# df1["sepal_length"].plot()
# 分析负数原因
index = df1[df1["sepal_length"] < 0].index
df2 = df1.drop(index)

indexsw = df2[df2["sepal_width"] > 5].index
df3 = df2.drop(indexsw)
indexpw = df3[df3["petal_width"] > 5].index
df4 = df3.drop(indexpw)
df4["sepal_length"].hist(bins=20)
plt.show()
