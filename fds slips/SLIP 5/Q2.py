import pandas as pd
import numpy as np

data = {
    "Month" : ["Jan","Feb","Mar","Apr","May","June","July","Aug","Spet","Oct","Nov","Dec"],
    "Sales" : [10,14,25,26,35,37,39,19,16,85,17,56]
}

df = pd.DataFrame(data)
print("\nData Frame Created SuccessFully ")

print("\nOrignal DataFrame")
print(df)

Data_Range = df["Sales"].max() - df["Sales"].min()
Data_Var = np.var(df["Sales"])
Data_Std = np.std(df["Sales"])

print("\n Data Range Of Data Frame :-",Data_Range)
print("\n Data Range Of Data var :-",round(Data_Var,2))
print("\n Data Standard Of Data Std :-",round(Data_Std,2),"Lakh")

