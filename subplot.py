import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use('TkAgg')

fig, ax = plt.subplots(2, 3)
# for i in range(2):
#     for j in range(3):
#         ax[i, j].text(0.3, 0.5, str((i, j)), fontsize=11)

grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
# 정규분포 데이터
x = np.random.randn(100)
y = np.random.randn(100)
plt.subplot(grid[0, 0]).scatter(x, y)

x = np.arange(10)
y = np.random.uniform(1, 10, 10)
plt.subplot(grid[0, 1:]).bar(x, y)

x = np.linspace(0, 10, 100)
y = np.cos(x)
plt.subplot(grid[1, :2]).plot(x, y)

z = np.random.uniform(0, 1, (5, 5))
plt.subplot(grid[1, 2]).imshow(z)

# 실선 그래프
plt.show()
