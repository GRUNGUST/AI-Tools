import pandas as pd
import numpy as np

# df = pd.DataFrame([[1, None], [np.nan, 4]])
# print(df)


## 寻找NaN
# print(df.isna())
# print(df.notna())

## 移除NaN
# df = pd.DataFrame({
#     "a": [1, None, 3],
#     "b": [4, 5, 6]
# })
# print(df)
# print(df.dropna(axis=0))
# print(df.dropna(axis=1))


## 填充NaN
# 使用平均值来填充
# df = pd.DataFrame({
#     "a": [1, None, 3],
#     "b": [4, 5, 6]
# })
# a_mean = df["a"].mean()
# new_col = df["a"].fillna(a_mean)
# df["a"] = new_col
# print(df)

# 找规律填充
# df = pd.DataFrame({
#     "a": [1, None, 3, None],
#     "b": [4, 8, 12, 12]
# })
# a_nan = df["a"].isna()
# a_new_value = df["b"][a_nan] / 4
# new_col = df["a"].fillna(a_new_value)
# df["a"] = new_col
# print(df)

# a_nan = df["a"].isna()
# df.loc[a_nan, "a"] = df["b"][a_nan] / 4

## 不符合范围的值
df = pd.DataFrame({
    "a": [1, 1, 2, 1, 2, 40, 1, 2, 1]
})
df["a"] = df["a"].clip(lower=0, upper=3)
print(df)
