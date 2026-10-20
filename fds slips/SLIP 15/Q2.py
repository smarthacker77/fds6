
import pandas as pd
Data = {
    "Emp_name" : ["Atharv","Ankit","Roshan","Darshan","Hitesh"],
    "Salary" : [35000,34000,10000,23000,24000]
}

df = pd.DataFrame(Data)
df.to_csv('Data_csv', index = False)
df = pd.read_csv('Data_csv')

print("Complete DataFrame:")
print(df)

print("\nDescriptive Statistics:")
print(df.describe())

print("\nFirst Five Records:")
print(df.head())

print("\nLast Five Records:")
print(df.tail())

print("\nMaximum Values:")
print(df.max(numeric_only=True))

print("\nMinimum Values:")
print(df.min(numeric_only=True))
