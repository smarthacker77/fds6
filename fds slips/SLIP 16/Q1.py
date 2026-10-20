
import pandas as pd

data = {
    'Rollno': [1, 2, 3, 4, 5],
    'Name': ['Rahul', 'Amit', 'Priya', 'Sneha', 'Rohit'],
    'Mark1': [80, 75, 90, 85, 70],
    'Mark2': [85, 80, 88, 90, 75],
    'Mark3': [78, 82, 92, 86, 72]
}

df = pd.DataFrame(data)

print("Student DataFrame:")
print(df)

print("\nMaximum Values:")
print(df.max(numeric_only=True))

print("\nMinimum Values:")
print(df.min(numeric_only=True))

print("\nDescriptive Statistics:")
print(df.describe())

print("\nShape of DataFrame:")
print(df.shape)
