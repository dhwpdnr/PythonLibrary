import pandas as pd
import numpy as np

path = "./data/"
name = "life_expectancy.csv"

read_fileName = path + name

df = pd.read_csv(read_fileName)

df_life = df["Life expectancy"]

ave_df_life = df_life.mean()