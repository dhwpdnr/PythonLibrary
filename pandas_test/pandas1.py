import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

month = pd.Series(["1월", "2월", "3월", "4월"])
income = pd.Series([9500, 6200, 6050, 7000])
expense = pd.Series([5040, 2350, 2300, 4800])

print("리스트")
df_1 = pd.DataFrame([month, income, expense])
print(df_1)
print("딕셔너리")
df_2 = pd.DataFrame({'월': month, '수입': income, '지출': expense})
print(df_2)
