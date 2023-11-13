import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use('TkAgg')
# 2행 2열의 그림 그리는 공간 생성
fig, ax = plt.subplots(2, 2)

x = np.random.randn(100)  # 정규분포 데이터
y = np.random.randn(100)  # 정규분포 데이터
# 산점도 그림
ax[0, 0].scatter(x, y)

x = np.arange(10)  # 0에서 9사이 연속값
y = np.random.uniform(1, 10, 10)  # 균일 분포 값
# 막대 그래프
ax[0, 1].bar(x, y)

x = np.linspace(0, 10, 100)
y = np.cos(x)
# 실선 그래프
ax[1, 0].plot(x, y)

z = np.random.uniform(0, 1, (5, 5))
ax[1, 1].imshow(z)

plt.show()