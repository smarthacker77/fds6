import pandas as pd

df = pd.read_csv("employees.csv")

print(df.describe())
print(df.mean(numeric_only=True))
print(df.isnull().sum())