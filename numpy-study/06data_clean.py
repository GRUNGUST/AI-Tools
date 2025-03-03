import numpy as np

raw_data = [
    ["Name", "StudentID", "Age", "AttendClass", "Score"],
    ["小明", 20131, 10, 1, 67],
    ["小花", 20132, 11, 1, 88],
    ["小菜", 20133, None, 1, "98"],
    ["小七", 20134, 8, 1, 110],
    ["花菜", 20134, 98, 0, None],
    ["刘欣", 20136, 12, 0, 12]
]

# data = np.array(raw_data)
# print(data.dtype)

# test1 = np.array([1, 2, 3])
# test2 = np.array([1.1, 2.3, 3.4])
# test3 = np.array([1, 2, 3], dtype=np.float64)
# print("test1.dtype", test1.dtype)
# print("test2.dtype", test2.dtype)
# print("test3.dtype", test3.dtype)

# object无法参与计算
# print("data >2", data > 2)


# 数据预处理
# 将数据dtype转为float64
data_process = []
for i in range(len(raw_data)):
    if i == 0:
        continue
    data_process.append(raw_data[i][1:])
data = np.array(data_process, dtype=np.float64)
# print("data.dtype", data.dtype)
# print(data)


# 清洗数据
# 寻找重复元素
# sid = data[:, 0]
# unique, counts = np.unique(sid, return_counts=True)
# print(counts)
# print(unique[counts > 1])

data[4, 0] = 20135
# print(data)


# 填补空age
is_nan = np.isnan(data[:, 1])
# print("is_nan", is_nan)
# nan_idx = np.argwhere(is_nan)

# ~ 对调True和False
# 计算有age值的平均值
# mean = data[~np.isnan(data[:, 1]), 1].mean()
# 平均值27.8，数据不正常
# print(mean)

normal_age_mask = ~np.isnan(data[:, 1]) & (data[:, 1] < 20)
# print("normal_age_mask", normal_age_mask)

# data[normal_age_mask,1]
# normal_age_mask [ True  True False  True False  True]
# 自动将筛选条件为False的元素剔除
normal_age_mean = data[normal_age_mask, 1].mean()
# print("normal_age_mean", normal_age_mean)

data[~normal_age_mask, 1] = normal_age_mean
# print("age: ", data)

# print(data[-3:, 2:])

# 没上课的成绩转成nan
data[data[:, 2] == 0, 3] = np.nan

# 超过100分和低于0分都处理
# 超过100会自动转成100，低于0会自动转成0
data[:, 3] = np.clip(data[:, 3], 0, 100)

print(data[:, 2:])
