import pandas as pd

Data = {
    "name" : ["Shyam","Shreeji","Ramya","Radha","Satya"],
    "Address" : ["Pune","Mumubai","Delhi","Mumbai","Pune"],
    "Age" : [20,19,None,21,22],
    "Class" :["BSc(Chemistry)","BSc(Physics)","BSc(Biology)","BSc(Zoology)","BSc(CS)"]
}

df = pd.DataFrame(Data)
df.to_csv("Student_Data_Csv",index= False)
df = pd.read_csv("Student_Data_Csv")
print("\n Orignal CSV Data Frame")
print(df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df = pd.get_dummies(df,columns = ["Address"], dtype = int)
print("\n After The One Hot Encoding :")
print(df)

df = pd.read_csv("Studen_Data_Csv",index = False)
