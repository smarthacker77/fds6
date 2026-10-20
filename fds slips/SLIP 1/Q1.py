import pandas as pd

data = {
    "Emp_name" : ["Atharv","Darshan","Ankit","Harshal","Sarthak","Kapil","Hitesh","Krish"],
    "Department" : ["IT","HR","Finance","Computer","IT","Finance","HR","Computer"],
    "Emp_name" : ["Devloper","Sales Excutive","Excutive","Recurtier","Analysist","Devloper","CA"],
    "Emp_name" : [76000,49000,67000,57000,89000,78000,85000,90000]
}

df = pd.DataFrame(data)

print("\nOriginal DataFrame")
print(df)

print("\nTop Five Records Of DataFrame")
print(df.head())
