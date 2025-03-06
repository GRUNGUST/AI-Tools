import pandas as pd
import numpy as np

# l = [11, 22, 33]
# s = pd.Series(l)
# print(s)

# 自定义索引
# s = pd.Series(l, ['a', 'b', 'c'])
# print(s)

# s = pd.Series({'a': 11, 'b': 22, 'c': 33})
# print(s)


# s = pd.Series(np.random.rand(3), index=["a", "b", "c"])
# print(s)

# 转化为numpy、list
# print("array:", s.to_numpy())
# print("list:", s.values.tolist())


## dataFrame
# df = pd.DataFrame([
#     [1, 2],
#     [3, 4]
# ])

# print(df)
# print(df.at[0, 1])

# df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]})
# print(df)

# print(df["col1"], "\n")
# print("取出来之后的 type：", type(df["col1"]))

# df = pd.DataFrame({"col1": pd.Series([1, 3]), "col2": pd.Series([2, 4])})
# print(df)

s = pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"])
df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]}, index=["a", "b"])
# print(s, "\n")
# print(df)

print(df.index, "\n")
print(df.columns)

n = df.to_numpy()
print(n)
