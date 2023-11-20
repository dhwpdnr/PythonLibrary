import pandas as pd
import numpy as np

path = "./data/"
name = "weather.csv"

read_fileName = path + name

df = pd.read_csv(read_fileName, encoding="CP949")

print(df.describe())

df["month"] = pd.DatetimeIndex(df["일시"]).month
df["year"] = pd.DatetimeIndex(df["일시"]).year

# monthly_means = df.groupby("month").mean()
