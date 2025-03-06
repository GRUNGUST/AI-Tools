import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import common as com

movies = pd.read_csv('data/imdb_top_1000.csv')
# print("数据维度:", df.shape)
# print(df.head)


## 数据清洗
# 查找缺失值 Certificate Meta_score Gross
# print(movies.isna().any())
# print(movies.isnull().sum())


# 删除无关列
movies.drop(["Poster_Link", "Overview", "Director", "Star1", "Star2", "Star3", "Star4"],
            inplace=True, axis=1)

# 删除缺失行
movies.dropna(subset=['Gross'], inplace=True)

movies['Gross'] = movies['Gross'].str.replace('[^\\d]', '', regex=True)
movies['Gross'] = movies['Gross'].str.strip()

movies["Gross"] = movies["Gross"].astype("int64")
# movies["Gross"] = pd.to_numeric(movies["Gross"], errors='coerce').astype('Int64')
# movies['Gross'] = pd.to_numeric(movies['Gross'], errors='coerce').fillna(0).astype('int64')

# 票房前十的电影
top = movies.sort_values("Gross", ascending=False).head(10)
# print(top)

# 不同电影类型的平均评分
genre_rating = movies.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False)

## 画图
# 柱状图
# 票房前十的电影
# plt.bar(top['Series_Title'], top['Gross'], color='skyblue')
# plt.xlabel('Gross(USD)')
# plt.xticks(rotation=45)


# plt.barh(top['Series_Title'], top['Gross'], color='green')
# plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(com.format_func))
# plt.ylabel('Gross(USD)')
# plt.title('Top 10 Movies by Gross')
# plt.show()


# 不同电影类型的平均评分
plt.bar(genre_rating.index[:10], genre_rating.values[:10])
plt.xlabel('Genre')
plt.xticks(rotation=45)
plt.show()
