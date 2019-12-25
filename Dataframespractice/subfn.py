import pandas as pd
import numpy as np
df1 = pd.DataFrame({"A":[1,2,3,4,5],
                    "B":[6,7,3,4,6],
                    "C":[5,8,7,9,4],
                    "D":[7,9,3,4,5]},index=["A1","A2","A3","A4","A5"])
print(df1)
print("-------------------")
sr = pd.Series([12,25,26,49],index=["A","B","C","D"])
print(sr)
print("-------------------")
df2 = df1.sub(sr, axis = 1)
print(df2)
print("-------------------")
df3 = pd.DataFrame({"A":[4,5,6,4,5],
                    "B":[6,7,3,4,6],
                    "C":[5,8,7,9,4],
                    "D":[7,9,3,4,5]},index=["A1","A2","A3","A4","A5"])

df4 = df1.sub(df3)
print(df4)