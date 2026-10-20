import pandas as pd

data = {
    "--:Laptop_model:--" : ["HP","Leveno","Asus","Acer","Dell"],
    "--:Price:--" : [80000,75000,95000,110000,85000]
}

df = pd.DataFrame(data)
print("\n Data Frame Are Created SucessFully :")

print("\n The Orignal Data Frame :")
print(df)
