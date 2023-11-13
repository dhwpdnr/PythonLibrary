import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use('TkAgg')
x = np.arange(-20, 20)
y1 = 2 * x
y2 = (1 / 3) * x ** 2 + 5
y3 = -x ** 2 - 5

plt.plot(x, y1, "g--", x, y2, "r^-", x, y3, "b*:")
plt.axis([-30, 30, -30, 30])
plt.show()
