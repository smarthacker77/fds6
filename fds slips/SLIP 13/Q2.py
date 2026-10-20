import pandas as pd 
from sklearn.preprocessing import LabelEncoder

Data = {
    "Contry" : ["India", "USA","UK","India","USA"],
    "Purcesd" : ["Yes","No","Yes","No","Yes"]
}

df = pd.DataFrame(Data)
df.to_csv('Data_csv', index = False)
df = pd.read_csv('Data_csv')
print("\n Orignal Csv Data Frame")
print(df)

df = pd.get_dummies(df, columns =["Contry"], dtype = int)
print("\n After The Data Frame One Hot Encoding ")
print(df)

le = LabelEncoder()
df["Purcesd"] = le.fit_transform(df["Purcesd"]) 
print("\n After lebel Encoding ")
print(df)
