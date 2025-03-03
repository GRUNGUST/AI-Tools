import pandas as pd
import numpy as np

# a_array = np.array([
#     [1, 2],
#     [3, 4]
# ])
#
# a_df = pd.DataFrame({
#     "a": [1, 3],
#     "b": [2, 4]
# })
#
# print("numpy array:\n", a_array)
# print("\npandas df:\n", a_df)


## 读取
# df = pd.read_excel("data/体检数据.xlsx", index_col=0)
# print(df)
#
# df.loc[2, "体重"] = 1
# print(df)
# df.to_excel("data/体检数据_修改.xlsx")

# with open("data/体检数据.csv", "r", encoding="utf-8") as f:
#     print(f.read())

# df_csv = pd.read_csv("data/体检数据.csv", index_col=0)
# df_csv.to_csv("data/体检数据_change.csv")
# print(df_csv)

#获取剪切板内容
# df = pd.read_clipboard()
# print(df)

df = pd.read_html("https://mofanpy.com/tutorials/data-manipulation/pandas/read-save/")
print(df)
