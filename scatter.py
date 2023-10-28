import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use('TkAgg')

n = 30  # 전체 점의 개수
x = np.random.rand(n)  # 점들의 임의 x 좌표
y = np.random.rand(n)  # 점들의 임의 y 좌표
colors = np.random.rand(n)  # 랜덤 색상
area = (30 * np.random.rand(n)) ** 2  # 반지름이 0~15 포인트 범위

plt.scatter(x, y, s=area, c=colors, alpha=0.5)

plt.show()
