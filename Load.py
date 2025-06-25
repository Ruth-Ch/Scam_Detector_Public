import pandas as pd
import numpy as np


df = pd.read_csv("SMS_Dataset/Dataset.csv")
cleaned = df.columns.tolist()
cleaned.remove('EMAIL')
df['PHONE'] = df['PHONE'].map({'yes': '1', 'No': '0'})
df['URL'] = df['URL'].map({'yes': '1', 'No': '0'})
df[cleaned].to_csv("SMS_Dataset/Dataset_Cleaned.csv", index = False)
print(df[cleaned].head())
