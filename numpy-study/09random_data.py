import random
import numpy as np

# print(random.random())
# print(random.randint(1, 10))
# print(np.random.randint(low=3, high=6, size=10))
dim1, dim2 = 3, 2
# print(np.random.rand(dim1, dim2))
# print(np.random.random([dim1, dim2]))

# 标准正态分布
# print(np.random.randn(dim1, dim2))


## 给你施加随机
data = np.array([2, 1, 3, 4, 6])
# print(np.random.choice(data))
# print("不重复地选多个(不放回)：", np.random.choice(data, size=3, replace=False))
# print("带权重地选择：", np.random.choice(data, size=10, p=[0, 0, 0, 0.2, 0.8]))

# data_copy = np.copy(data)
# 重新排序
# np.random.shuffle(data)
# print("源数据：", data_copy)
# print("shuffled:", data)

# print("直接出乱序序列：", np.random.permutation(10))
# data = np.arange(12).reshape([6, 2])
# print("多维数据在第一维度上乱序：\n", np.random.permutation(data))


# print("正态分布：", np.random.normal(1, 0.2, 10))
# print("均匀分布：", np.random.uniform(-1, 1, 10))


np.random.seed(2)
print(np.random.randint(2, 10, size=3))
np.random.seed(2)
print(np.random.randint(2, 10, size=3))
