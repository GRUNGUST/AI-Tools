import numpy as np

# data = np.random.rand(4, 3)
# weights = np.random.rand(3, 2)
# # 4*3 * 3*2
# output = np.dot(data, weights)
# print("data shape:", data.shape)
# print("weights shape:", weights.shape)
# print("output shape:", output.shape)


# 这个 student 数据是我随便编的，它有三个特征值，可能可以代表前几次考试的成绩。
# model 里安放的是模型的权重值等，而 score 就是计算得出的预测分数了。
student = np.array([[1, 2, 3]])
model = np.random.rand(3, 1)
score = np.dot(student, model)
print(score)

