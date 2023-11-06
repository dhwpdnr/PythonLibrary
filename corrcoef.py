import numpy as np

rng = np.random.default_rng(seed=42)
xarr = rng.random((3, 3))
R1 = np.corrcoef(xarr)

x = np.arange(0, 10)
y = x * 2

r_coef = np.corrcoef(x, y)
print(r_coef)
