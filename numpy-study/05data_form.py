import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
# 添加维度
# 列项拓展
# a_2d = a[np.newaxis, :]

# 横项拓展
# a_none = a[:, None]
# a_expand = np.expand_dims(a, axis=1)

# 减少维度
# a_squeeze = np.squeeze(a_expand)
# a_squeeze_axis = a_expand.squeeze(axis=1)


#
# a1 = a.reshape([2, 3])
# a2 = a.reshape([3, 1, 2])
# print(a1)
# print(a2)

# 转置
# a = np.array([1, 2, 3, 4, 5, 6]).reshape([2, 3])
# aT1 = a.T
# aT2 = np.transpose(a)
# print(a)
# print(aT1)
# print(aT2)


##合并
# 会帮你自动处理维度信息
# feature_a = np.array([1, 2, 3, 4, 5, 6])
# feature_b = np.array([11, 22, 33, 44, 55, 66])
#
# c_col = np.column_stack([feature_a, feature_b])
# c_row = np.row_stack([feature_a, feature_b])
# print(c_col)
# print(c_row)


# 需要手动处理维度信息
# feature_a = np.array([1, 2, 3, 4, 5, 6])[:, None]
# feature_b = np.array([11, 22, 33, 44, 55, 66])[:, None]
# c_stack = np.hstack([feature_a, feature_b])
# print(c_stack)


# a = np.array([
#     [1, 2],
#     [3, 4]
# ])
# b = np.array([
#     [5, 6],
#     [7, 8]
# ])
#
# print(np.concatenate([a, b], axis=0))
# print(np.concatenate([a, b], axis=1))


##拆解
a = np.array(
    [[1, 11, 2, 22],
     [3, 33, 4, 44],
     [5, 55, 6, 66],
     [7, 77, 8, 88]]
)

# 横向切分
#print(np.vsplit(a, indices_or_sections=2))
# 分片成[:2],[2:3],[3:]
#print(np.vsplit(a, indices_or_sections=[2, 3]))

print(np.split(a, indices_or_sections=2, axis=0))
print(np.split(a, indices_or_sections=[2, 3], axis=1))
