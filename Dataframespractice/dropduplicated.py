import pandas as pd
data = pd.read_csv("/Users/suprithmekala/Desktop/employees.csv")
df = pd.DataFrame(data)
data.sort_values("First Name",inplace=True)
data.drop_duplicates(subset="First Name",keep = False, inplace=True)
print(data)
