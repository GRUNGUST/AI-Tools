import numpy as np

# a = np.array([1, 2, 3])
# print("a[0]:", a[0])
# print("a[1]:", a[1])
#
# print("a[[0,1]]:\n", a[[0, 1]])
# print("a[[1,1,0]]:\n", a[[1, 1, 0]])

# b = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ])
#
# # 第2行第3个，第1行第4个
# print("b[[1,0],[2,3]]:\n", b[[1, 0], [2, 3]])


# 切片
# a = np.array([1, 2, 3])
# print("a[0:2]:\n", a[0:2])
# print("a[1:]：\n", a[1:])
# print("a[-2:]：\n", a[-2:])

# b = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ])
#
# # 第1行到第2行
# print("b[:2]:\n", b[:2])
# # 第1行到第2行，第1列到第2列
# print("b[:2, :3]:\n", b[:2, :3])
# # 第2行到第3行，倒数第2列和倒数第1列
# print("b[1:3, -2:]:\n", b[1:3, -2:])


# 筛选
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# 序列
# print(a[a > 7])


# condition = a > 7
# print(condition)
#
# condition = (a > 7) & (a != 10)
# print(a[condition])


# 符合条件的都换成-1
condition = a > 7
# print(np.where(condition, -1, a))

# 不符合条件的换成2
# print(np.where(condition, -1, 2))

# 不符合条件执行b值的运算
b = -a - 1
print(np.where(condition, a, b))
