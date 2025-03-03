import numpy as np
import matplotlib
with open('day_wise.csv', 'r', encoding='utf - 8') as f:
    data = f.readlines()

covid = {
    "date": [],
    "data": [],
    "header": data[0].strip().split(",")[1:]
}

for row in data[1:]:
    split_row = row.strip().split(",")
    covid["date"].append(split_row[0])
    covid["data"].append([float(n) for n in split_row[1:]])

data = np.array(covid["data"])
# 2020年2月3日的所有数据
# print("日期列表摘取：", covid["date"][:4])
#
# date_idx = covid["date"].index("2020-02-03")
# print("日期->索引 转换：", date_idx)
#
# for header, number in zip(covid["header"], data[date_idx]):
#     print(header, ":", number)


# 2020年1月24日之前的累积确诊病例有多少个
# row_idx = covid["date"].index("2020-01-24")
# column_idx = covid["header"].index("Confirmed")
# confirmed0124 = data[row_idx, column_idx]
# print("截止 1 月 24 日的累积确诊数：", confirmed0124)

# 2020年7月23日的新增死亡数是多少
# row_idx = covid["date"].index("2020-07-23")
# column_idx = covid["header"].index("New deaths")
# new_deaths0723 = data[row_idx, column_idx]
# print(" 7 月 23 日的新增死亡数：", new_deaths0723)


## 总增长数
# 从 1 月 25 日到 7 月 22 日，一共增长了多少确诊病例？
# row1_idx = covid["date"].index("2020-01-25")
# row2_idx = covid["date"].index("2020-07-22")
# new_cases_idx = covid["header"].index("New cases")
#
# new_cases = data[row1_idx:row2_idx + 1, new_cases_idx]
# overall = sum(new_cases)
# print("共增长：", overall)

# confirmed_idx = covid["header"].index("Confirmed")
# confirmed_data = data[:, confirmed_idx]
# overall = confirmed_data[row2_idx] - confirmed_data[row1_idx]
# print("共增长：", overall)

# 对比差异
# confirmed = data[:, confirmed_idx]
# new_cases = data[:, new_cases_idx]
# for i in range(row1_idx, row2_idx + 1):
#     diff = new_cases[i] - (confirmed[i] - confirmed[i - 1])
#     if diff != 0:
#         print("date index: ", i, "diff: ", diff)


##确诊恢复比例
# 每天新增确诊数和新恢复数的比例？平均比例，标准差各是多少？
new_cases_idx = covid["header"].index("New cases")
new_recovered_idx = covid["header"].index("New recovered")

# 比例
# ratio = data[:, new_cases_idx] / data[:, new_recovered_idx]
# print(ratio[:5])
# print(data[0, new_cases_idx])
# print(data[0, new_recovered_idx])

not_zero_mark = data[:, new_recovered_idx] != 0
ratio = data[not_zero_mark, new_cases_idx] / data[not_zero_mark, new_recovered_idx]

# 平均比例
ratio_mean = ratio.mean()
ratio_std = ratio.std()
print("平均比例：", ratio_mean, "标准差", ratio_std)


