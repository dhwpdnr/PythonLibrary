import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use('TkAgg')

data = [5, 4, 6, 11]
clist = ["cyan", "gray", "orange", "red"]
explode = [.06, .07, .08, .09]
plt.pie(data, autopct="%.2f%%", colors=clist, labels=clist, explode=explode)

plt.show()
