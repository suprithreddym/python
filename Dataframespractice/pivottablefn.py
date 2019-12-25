import pandas as pd
import numpy as np
df1 = pd.read_csv("/Users/suprithmekala/Desktop/employees.csv")
print(df1.head())
print("--------------------")
df2 = pd.pivot_table(df1, index=['First Name'])
print(df2)
print("--------------------")
a_3 = pd.pivot_table(df1,index=['First Name','Gender'],values=["Bonus %"],aggfunc=np.mean)
print(a_3)
print("--------------------")
a_4 = pd.pivot_table(df1, index=['First Name','Gender'], values=["Salary","Bonus %"],aggfunc=[np.sum,np.mean],fill_value=0,margins=True)
print(a_4)
print("--------------------")
a_5 = a_4.query('Gender == ["Male"]')
print(a_5)