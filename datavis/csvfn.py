import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/suprithmekala/Desktop/train.csv")
print(df.head())
df["Age"].hist(bins=20)  # histogram
df.plot.line(x='Age', y='Fare', figsize=(8, 6), title='suppu')  # line
df.plot.scatter(x='Age', y='Fare', figsize=(8, 6))  # scatter
df.plot.box(figsize=(10, 8))  # box
df.plot.hexbin(x='Age', y='Fare', gridsize=30, figsize=(8, 6))  # hexagonal
plt.show()
