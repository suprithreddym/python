import pandas as pd
a_1 = ['Siva','Sunitha','suprith','sunny','sowmya']
df1 = pd.DataFrame(a_1)
print(df1)
print("---------------------------------")
a_2 = {'name': ['Siva','Sunitha','suprith','sunny','sowmya'],
       'Age': ['58','50','25','21','25']}
df2 = pd.DataFrame(a_2)
print(df2)
print("---------------------------------")
a_3 = {'name': ['Siva','Sunitha','suprith','sunny','sowmya'],
       'Age': ['58','50','25','21','25'],
       'Address':['piler','piler','piler','piler','nellore']}
df3 = pd.DataFrame(a_3)
print(df3[['name','Address']])
print("---------------------------------")
a_4 = pd.read_csv("/Users/suprithmekala/Desktop/movies.csv")
df4 = pd.DataFrame(a_4)
print(df4)
print("---------------------------------")
first = df4.iloc[0]
print(first)
print("---------------------------------")
a_5 = df4.index
a_6 = df4.columns
print(a_5)
print(a_6)
print("---------------------------------")
a_7 = pd.DataFrame(df4, columns=['Title','Actor 1'], index=[10])
print(a_7)
print(a_7.values)
print("---------------------------------")
df5 = df4.isnull()
print(df5)
print("---------------------------------")
df6 = df4.fillna(0)
print(df6)
print("---------------------------------")
for i,j in df2.iterrows():
    print(i,j)
print("---------------------------------")
df7 = df6.head()
print(df7)

#DataFrameName.insert(loc, column, value, allow_duplicates = False)

print("---------------------------------")
df7.insert(1,"Team",[1,2,3,4,5])
print(df7)