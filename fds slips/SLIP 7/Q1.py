import pandas as pd

Staff_Data = {
    "Staff_Id" : [101,102,103,104,105],
    "Emp_Name" : ["Atharv","Ankit","Roshan","hitesh","Krish"],
    "Department" : ["HR","IT","Finance","Computer","IT"],
    "Salary" : [95000,57000,85000,89000,67000]
}

df = pd.DataFrame(Staff_Data)
print("\n Orignal Data Frame")
print(df)

df.to_csv('Staff_CSV',index= False)
print("\n Data Frame Into CSV")

Staff = pd.read_csv('Staff_CSV')
print("\n Staff CSV Data Frame ")
print(Staff)

