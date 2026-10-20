import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "Name" : ["Samran","Sachin","Samarpan","Spandan","Sharvan"],
    "Address" : ["Pune", "Mumbai","Delhi","Madurai","Chennai"],
    "Age" : [20, 23, 19, 21,22],
    "Class" : ["BE","BSc(CS)","BVoC","BCom","BSc"]
}

df = pd.DataFrame(data)

df.to_csv('StudentData_csv',index=False)
print("\nStudentData_csv Are Created SucssesFully")

df = pd.read_csv('StudentData_csv')
print("\nOrignal DataSet")
print(df)

df_Encoded = pd.get_dummies(df, columns = ["Name"], dtype = int)
print("\nAfter One_Hot Encoding")
print(df_Encoded)

le = LabelEncoder()
df_Encoded['Class'] = le.fit_transform(df_Encoded['Classs'])
print("\nAfter Label Encoding")
print(df_Encoded)