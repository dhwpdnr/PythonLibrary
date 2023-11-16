import pandas as pd
import numpy as np

path = "./data/"
name = "life_expectancy.csv"

read_fileName = path + name

df = pd.read_csv(read_fileName)

above_65_df = df[df["Life expectancy"] > 65]
above_65_70_df = df[df["Life expectancy"].isin([65, 70])]
country_angola = df[df["Country"].isin(["Angola"])]
