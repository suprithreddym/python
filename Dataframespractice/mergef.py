import pandas as pd
df1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                    'key2': ['K0', 'K1', 'K0', 'K1'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})

df2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                    'key2': ['K0', 'K0', 'K0', 'K0'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})
res = pd.merge(df1,df2,on=['key1','key2'])
print(res)
print("------------------------")
a_1 = pd.merge(df1,df2,how = 'left',on=['key1','key2'])
print(a_1)
print("------------------------")
a_2 = pd.merge(df1,df2,how = 'right',on=['key1','key2'])
print(a_2)
print("------------------------")
a_3 = pd.merge(df1,df2,how = 'outer',on=['key1','key2'])
print(a_3)
print("------------------------")
a_4 = pd.merge(df1,df2,how = 'inner',on=['key1','key2'])
print(a_4)