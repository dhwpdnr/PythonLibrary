import pandas as pd
import numpy as np

file_path = "./data/vehicle_prod.csv"
file_name = "vehicle.csv"

df = pd.read_csv(file_path)

save_fileName = file_path + "data2.csv"
df.to_csv(save_fileName, index=False)

save_fileName2 = file_path + "data2.xlsx"
df.to_excel(save_fileName2, sheet_name="mySheet", index=False)
print(df)
