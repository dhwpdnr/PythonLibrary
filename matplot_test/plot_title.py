import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use('TkAgg')

x = np.linspace(0, np.pi * 2, 100)

# 제목 설정
plt.title("sin cos curve")

# sin 그래프
plt.plot(x, np.sin(x), "r-", label="sin curve")

# cos 그래프
plt.plot(x, np.cos(x), "b:", label="cos curve")

# x축 라벨 설정
plt.xlabel("x value")
# y축 라벨 설정
plt.ylabel("y value")
# 범례 추가
plt.legend()

plt.style.use("dark_background")

plt.show()
