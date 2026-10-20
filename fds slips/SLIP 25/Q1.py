import pandas as pd

df = pd.DataFrame({
    'Product': ['Pen', 'Book', 'Bag', 'Pencil', 'Scale'],
    'Quantity': [10, 5, 3, 8, 4],
    'Price': [10, 50, 500, 5, 20]
})

print(df)
print("Total Quantity:", df['Quantity'].sum())
print("Average Price:", df['Price'].mean())