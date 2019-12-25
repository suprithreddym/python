#unique
import numpy as np
import pandas as pd
df = pd.DataFrame({"A":[14, 4, 5, 4, 1],
                   "B":[5, 2, 54, 3, 2],
                   "C":[20, 20, 7, 3, 8],
                   "D":[14, 3, 6, 2, 6]})
print(df)

print("-----------------------")
print(df.nunique(axis=1))
print("-----------------------")
df1 = pd.DataFrame({"A":["Sandy", "alex", "brook", "kelly", np.nan],
                   "B":[np.nan, "olivia", "olivia", "", "amanda"],
                   "C":[20 + 5j, 20 + 5j, 7, None, 8],
                   "D":[14.8, 3, None, 6, 6]})

print(df1.nunique(axis=0, dropna=True))
print("-----------------------")
a_1 = pd.read_csv("/Users/suprithmekala/Desktop/movies.csv")
df2 = pd.DataFrame(a_1)
print(df2)
print("-----------------------")
#displays data of year is nan
df3 = pd.notnull(df2['Year'])
print(df2[df3])
print("-----------------------")
df4 = df2['IMDB Score'].between(6,7,inclusive=True)
print(df2[df4])
print("-----------------------")
print(df2[:10])
print("-----------------------")
before = type(df2.Year[0])
print(before)
df2 = df2.dropna()
df2.Year = df2.Year.astype('int64')
after = type(df2.Year)
print(after)
print(df2.info())
print("-----------------------")
df3 = df1.sort_index(axis=1)
print(df3)
print("-----------------------")
df4 = pd.DataFrame(a_1)
new_df4 = df4.rename(columns = {"Title":"Name"})
print(new_df4)
print("-----------------------")
new_df4.drop(["Year"],axis=1,inplace=True)
print(new_df4)
print("-----------------------")
new_df4.pop("Name")
print(new_df4)
print("-----------------------")
row1 = df4.sample(n=1)
print(row1)
print("-----------------------")
#generate fraction of data
rows = df4.sample(frac=0.01)
print(rows)
print("-----------------------")
print(rows.sort_index())
#nsmallest
print("-----------------------")
least5 = df4.nsmallest(5, "IMDB Score")
print(least5)
print("-----------------------")
large5 = df4.nlargest(5, "IMDB Score")
print(large5)
print("-----------------------")
shape = df1.shape
size = df1.size
ndim = df1.ndim
print(shape)
print(size)
print(ndim)
# print("-----------------------")
# large5["Year"].fillna('2013',inplace = True)
# print(large5)
print("-----------------------")
large5["Year"].fillna(method='ffill' ,inplace = True)
print(large5)
#rank
print("-----------------------")
df4["Rank"] = df4["Title"].rank()
print(df4)
print("-----------------------")
#sort rank
df4.sort_values("Title",inplace=True)
print(df4)
#query
df4.columns = [column.replace("Title","Name") for column in df4.columns]
print(df4)
df4.query('Year == 2013.0' and 'Rank == 10.0',inplace=True)
print(df4)