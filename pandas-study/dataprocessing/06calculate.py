import pandas as pd
import numpy as np

# data = np.arange(-12, 12).reshape((6, 4))
# df = pd.DataFrame(
#     data,
#     index=list("abcdef"),
#     columns=list("ABCD"))
# print(df)
# df["A"] *= 0

# df.loc["a", "A"] = 100
# df.iloc[1, 0] = 200

# df.loc["a", :] = df.loc["a", :] * 2
# df.loc[df["A"] == 0, "A"] = -1
# print(df)

## apply
df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
print(df)


# print(np.sqrt(df))
# print(df.apply(np.sqrt))


# def func(x):
#     return x.iloc[0] * 2, x.iloc[1] * -1


# print(df.apply(func, axis=1, result_type='expand'))
# print(df.apply(func, axis=1, result_type='broadcast'))





# def func(x):
#     return x["A"] * 4
#
# print(df.apply(func, axis=1))
# df["A"] = df.apply(func, axis=1)
# print(df)

# def func(r):
#     return r[2] * 4


# last_row = df.apply(func, axis=0)
# print(last_row)

#df.iloc[2, :] = last_row
print(df)
