import numpy as np
import random

# zeros = np.zeros((2, 3))
# print(zeros)
#
# ones = np.ones((3, 2))
# print(ones)
#
# nines = np.full([2, 3], 9)
# print(nines)

# data = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64)
#
# ones = np.ones(data.shape, dtype=data.dtype)
# ones_like = np.ones_like(data)
# np.zeros_like(data)
# np.full(data, 6)


# print("python range:", list(range(5)))
# print("numpy arange:", np.arange(5))
#
# print("python range:", list(range(3, 10, 2)))
# print("numpy arange:", np.arange(3, 10, 2))


# 取5个数，从-1 到 1
# print("linespace:", np.linspace(-1, 1, 5))
# print("5 segments:", np.linspace(-1, 1, 5, endpoint=False))


## 快速创建
# print(np.empty([4, 3]))
empty = np.empty([2, 3])
print("empty before:\n", empty)
data = np.arange(6).reshape([2, 3])
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        empty[i, j] = data[i, j] * random.random()
print(empty)
