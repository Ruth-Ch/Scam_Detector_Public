import pandas as pd
import numpy as np


df = pd.read_csv("SMS_Dataset/Dataset.csv")
print(df.head())
cleaned = df.columns.tolist()
cleaned.remove('EMAIL')
print(df[cleaned].head())
df[cleaned].to_csv("SMS_Dataset/Dataset_Cleaned.csv", index = False)
