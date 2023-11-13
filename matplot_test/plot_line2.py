import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use('TkAgg')

n = 50
x = np.arange(n)
y = np.random.random(size=n)

plt.plot(x, y, "g^:")
plt.show()
