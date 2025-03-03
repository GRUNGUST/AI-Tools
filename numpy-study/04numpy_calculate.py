import numpy as np

# 批量运算
# a = np.array([150, 166, 183, 170])
# print(a + 3)

# a = np.array([
#     [1, 2],
#     [3, 4]
# ])
# b = np.array([
#     [5, 6],
#     [7, 8]
# ])

# 1*5+2*7  1*6+2*8
# 3*5+4*7  3*6+4*8
# print(a.dot(b))
# print(np.dot(a, b))


# 数据统计分析
# a = np.array([150, 166, 183, 170])
# print(a.sum())
# print("累乘：", a.prod())
# print("总数：", a.size)
#
# a = np.array([0, 1, 2, 3])
# print("非零总数：", np.count_nonzero(a))
#
# month_salary = [1.2, 20, 0.5, 0.3, 2.1]
# print("平均工资：", np.mean(month_salary))
# print("工资中位数：", np.median(month_salary))
#
# # (每个元素-平均数)的绝对值，绝对值之和除于元素个数
# print("标准差：", np.std(month_salary))


# a = np.array([150, 166, 183, 170])
# name = ["小米", "OPPO", "Huawei", "诺基亚"]
# # 最大值的位置和最小值的位置
# high_idx = np.argmax(a)
# low_idx = np.argmin(a)
# print("{} 最高".format(name[high_idx]))
# print("{} 最矮".format(name[low_idx]))

a = np.array([150.1, 166.4, 183.7, 170.8])
# 向上取整
# print("ceil:", np.ceil(a))
# print("floor:", np.floor(a))


# 夹子
print("clip:", a.clip(160, 180))
