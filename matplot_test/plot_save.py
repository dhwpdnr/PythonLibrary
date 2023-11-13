import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use('TkAgg')

x = np.linspace(0, np.pi * 2, 100)
# fig 객체 생성
fig = plt.figure()

# sin 그래프
plt.plot(x, np.sin(x), "r-")

# cos 그래프
plt.plot(x, np.cos(x), "b:")

# 저장
fig.savefig("sin_cos_fig.png")
plt.show()
