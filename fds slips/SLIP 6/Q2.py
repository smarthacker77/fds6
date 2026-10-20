
import pandas as pd

data = {
    'emp_name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan',
                 'Pooja', 'Karan', 'Neha', 'Vijay', 'Anita'],
    'age': [25, 30, 28, 35, 27, 32, 29, 31, 40, 26],
    'salary': [30000, 40000, 35000, 50000, 32000,
               45000, 38000, 42000, 60000, 33000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nShape of DataFrame:")
print(df.shape)

print("\nDescription of DataFrame:")
print(df.describe())

new_rows = pd.DataFrame({
    'emp_name': ['Amit', 'Rahul', None, 'Sneha', 'Vikas'],
    'age': [25, 30, 24, None, 33],
    'salary': [30000, 40000, 28000, 50000, None]
})

new_rows['Department'] = [None, None, None, None, None]

df['Department'] = None

df = pd.concat([df, new_rows], ignore_index=True)

print("\nFinal DataFrame with Duplicate and Missing Values:")
print(df)