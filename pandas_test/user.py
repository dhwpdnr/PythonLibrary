import pandas as pd
import numpy as np
import re

path = "./data/"
name = "user.csv"

read_fileName = path + name
df = pd.read_csv(read_fileName)
user_data = []
phone_numbers = set()
phone_regex = re.compile(r'^\d{10,11}$')

for item in df.itertuples():
    phone_number = str(item[3])
    if re.match(phone_regex, phone_number) and phone_number not in phone_numbers:
        user_payload = {
            "name": item[1],
            "phone_number": phone_number,
            "id": item[2]
        }
        user_data.append(user_payload)
        phone_numbers.add(phone_number)

print(user_data)
