import pandas as pd

df = pd.read_csv("employee.csv")

print(df)
print(df.describe())
print(df.head())
print(df.tail())
print(df.max(numeric_only=True))
print(df.min(numeric_only=True))