import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

# 1차 함수
# plt.plot([1, 2, 3, 4])
plt.ylabel("y label")
plt.xlabel("x label")
# plt.show()

# 2차 함수
x = np.arange(10)
plt.plot(x**2)

plt.show()
