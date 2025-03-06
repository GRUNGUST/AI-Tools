import numpy as np
import pandas as pd
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

## scatter
# n = 1024  # data size
# df = pd.DataFrame({
#     "x": np.random.normal(0, 1, n),
#     "y": np.random.normal(0, 1, n),
# })
# color = np.arctan2(df["y"], df["x"])
# df.plot.scatter(x="x", y="y", c=color, s=60, alpha=.5)
#
# plt.show()

## plot
n = 20  # data size
x = np.linspace(-1, 1, n)
y = x * 2 + 0.4 + np.random.normal(0, 0.3, n)
df = pd.DataFrame({
    "x": x,
    "y": y,
})
df.plot(x="x", y="y", alpha=.5, c="r")
plt.show()
