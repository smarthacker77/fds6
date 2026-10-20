import pandas as pd

Data = {
    "species" : ["Satosa","versicolor"]
}
df = pd.DataFrame(Data)
df.to_csv('iris_csv', index = False)
df = pd.read_csv('iris_csv')
print("\n Frequancy Of Iris Queris")
print(df["species"].value_counts())