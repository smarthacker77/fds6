
import pandas as pd

data = {
    'Name': ['Shrikrishna', 'Shridhar', 'Mohan',
             'Govind', 'Vasudev'],
    'Address': ['Trivendram', 'Madurai', 'Suchindram',
                'Rameswaram', 'Kanyakumari'],
    'Age': [20, None, 19, 21, 22],
    'Class': ['BE', 'BSc(CA)', 'BVoC', 'BCom', 'BSc']
}

df = pd.DataFrame(data)

df.to_csv('StudentData.csv', index=False)

print("StudentData.csv created successfully!")

df = pd.read_csv('StudentData.csv')

print("\nOriginal Dataset:")
print(df)

mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

print("\nDataset after replacing missing Age:")
print(df)

df.to_csv('StudentData.csv', index=False)

print("\nUpdated dataset saved successfully!")
