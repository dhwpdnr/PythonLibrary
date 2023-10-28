import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use('TkAgg')

x = np.arange(3)
years = ["2010", "2011", "2012"]
domestic = [6801, 7695, 8010]
foreign = [777, 1046, 1681]

plt.bar(x, domestic, width=0.25)
plt.bar(x + 0.3, foreign, width=0.25)
plt.xticks(x, years)

plt.show()
