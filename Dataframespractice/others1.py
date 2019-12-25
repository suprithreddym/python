import pandas as pd
import numpy as np
#copy
a_1 = pd.Series(['a','b','c','d'])
new = a_1.copy()
new[1] = 'Chnaged Value'
print(new)
print("--------------------")
print(a_1)
a_2 = pd.read_csv("/Users/suprithmekala/Desktop/employees.csv")
df1 = pd.DataFrame(a_2)
print("--------------------")
print(df1)
df1.sort_values("First Name", inplace=True)
bool_series = df1["First Name"].duplicated()
print("--------------------")
print(df1.head())
print("--------------------")
print(df1[bool_series])

# Removing duplicated
print("--------------------")
df2 = pd.DataFrame(a_2)
df2.sort_values("First Name",inplace=True)
bool_series1 = df2["First Name"].duplicated(keep= False)
print("--------------------")
print(bool_series1)
print("--------------------")
df2 = df2[~bool_series1]
print(df2)
print(df2.info())


