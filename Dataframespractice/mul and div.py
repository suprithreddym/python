import pandas as pd
df1=pd.DataFrame({"A":[14,4,5,4,1],
                  "B":[5,2,54,3,2],
                  "C":[20,20,7,3,8],
                  "D":[14,3,6,2,6]})
print(df1)
print("---------------------------")
sr = pd.Series([3, 2, 4, 5, 6])
df2 = df1.mul(sr, axis = 0 )
print(df2)
print("---------------------------")
df3 = pd.DataFrame({"A":[5, 3, 6, 4],
                   "B":[11, 2, 4, 3],
                   "C":[4, 3, 8, 5],
                   "D":[5, 4, 2, 8]})

df4 = df3.div(2)
print(df4)