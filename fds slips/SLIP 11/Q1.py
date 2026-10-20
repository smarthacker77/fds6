import pandas as pd
import numpy as np

Data = {
    "Month" : ["Jan","Feb","Mar","Apr","May","June","July","Aug","Spet","Oct","Nov","Dec"],
    "Sales" : [10,14,25,26,35,37,39,19,16,85,17,56]
}

df = pd.DataFrame(Data)
print("\n The Orignal Data Frame ")
print(df)

Data_Range = df["Sales"].max() - df["Sales"].min()
Data_Var = np.var(df["Sales"])
Data_Std = df["Sales"].std()

print("\n The Range Of Data Frame :-",Data_Range)
print("\n The Variance Of Data Frame :-",Data_Var)
print("\n The Standard Deviation Of Data Frame :-",Data_Std)

