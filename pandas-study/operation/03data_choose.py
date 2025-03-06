import pandas as pd
import numpy as np

data = np.arange(-12, 12).reshape((6, 4))
df = pd.DataFrame(data, index=list("abcdef"), columns=list("ABCD"))
# print(data)
# print(df)

## 选取数据
# print(df["B"])

# print(data[:, [2, 1]])
# print(df[["C", "B"]])

# data[2:3, 1:3]
# print(df.loc["c":"d", "B":"D"])


# print("numpy:\n", data[[3, 1], :])
# print("\ndf:\n", df.loc[["d", "b"], :])
#
# print("numpy:\n", data[2:3, 1:3])
# print("\ndf:\n", df.iloc[2:3, 1:3])

# row_labels = df.index[2:4]
# print("row_labels:\n", row_labels)
# print("\ndf:\n", df.loc[row_labels, ["A", "C"]])
#
# col_labels = df.columns[[0, 3]]
# print("col_labels:\n", col_labels)
# print("\ndf:\n", df.loc[row_labels, col_labels])

# col_index = df.columns.get_indexer(["A", "B"])
# print("col_index:\n", col_index)
# print("\ndf:\n", df.iloc[:2, col_index])

## 条件筛选
# print(df[df["A"] < 0])

# print("~:\n", df.loc[:, ~(df.iloc[0] < -10)])
# print("\n>=:\n", df.loc[:, df.iloc[0] >= -10])

i0 = df.iloc[0, 1]
# print(df.loc[:, ~(i0 < -10) | (i0 < -11)])

## Series 和 DataFrame
list_data = list(range(-4, 4))
s = pd.Series(
    list_data,
    index=list("abcdefgh"))
print(s)
# print(s.loc[["a", "g", "c"]], "\n")
# print(s.loc["c":"f"])

# print(s.iloc[[3, 1, 5]], "\n")
# print(s.iloc[2: 4])


print(s.iloc[s.index.get_indexer(["c", "d"])], "\n")
print(s.loc[s.index[[3, 2]]])
