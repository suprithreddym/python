import pandas as pd
import numpy as np
data = pd.read_csv("/Users/suprithmekala/Desktop/nba.csv")
df1 = pd.DataFrame(data)
df1.sort_values("Team",inplace=True)
filter = df1["Team"] == "Atlanta Hawks"
df1.where(filter, inplace=True)
print(df1)
print("--------------------")
filter1 = df1["Age"] > 24
df1.where(filter & filter1,inplace=True)
print(df1)
print("--------------------")
df2 = df1.dropna(subset=['Team','Age'])
print(df2)
print("--------------------")
df3 = df1.dropna()
print(df3)
