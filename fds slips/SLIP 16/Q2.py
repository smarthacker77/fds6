import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    'Country': ['India', 'USA', 'UK', 'India', 'USA'],
    'Purchased': ['Yes', 'No', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)

df.to_csv("data.csv", index=False)

df = pd.read_csv("data.csv")

print("Original Dataset:")
print(df)

df = pd.get_dummies(df, columns=['Country'], dtype=int)

le = LabelEncoder()
df['Purchased'] = le.fit_transform(df['Purchased'])

print("\nEncoded Dataset:")
print(df)
