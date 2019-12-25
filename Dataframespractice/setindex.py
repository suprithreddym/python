import pandas as pd
data = pd.read_csv("/Users/suprithmekala/Desktop/employees.csv")
df1 = pd.DataFrame(data)
df1.set_index("First Name", inplace=True, drop=False)
print(df1)

print("--------------------")
print(df1.index)

df2 = pd.DataFrame(data)
df2.set_index(["First Name","Gender"],inplace=True,append=False,drop=True)
print(df2)

print("--------------------")

df2.reset_index(inplace=True)
print(df2)