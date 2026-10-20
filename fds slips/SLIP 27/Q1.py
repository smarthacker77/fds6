import pandas as pd

df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [20, 50, 10, 40, 30]
})

print(df)
print("Maximum:", df['Value'].max())
print("Minimum:", df['Value'].min())