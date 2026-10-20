
import pandas as pd

data = {
    'emp_name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan',
                 'Pooja', 'Karan', 'Neha', 'Vijay', 'Anita'],
    'age': [25, 30, 28, 35, 27, 32, 29, 31, 40, 26],
    'salary': [30000, 40000, 35000, 50000, 32000, 45000, 38000, 42000, 60000, 33000]
}

df = pd.DataFrame(data)
print("\n Orignal Data Frame")
print(df)

print("\n Shape Of The Data Frame")
print(df.shape)

print("\n Describe Of The Data Frame")
print(df.describe())

df['Department'] = None

New_Data = pd.DataFrame({
    'emp_name' : ['Amit','Ankit','Roshan','Rahul','Hitesh'],
    'age' : [25, 37,20,30,None],
    'Salary' : [30000,38000,None,40000,35000],
    'Department' : [None,None,None,None,None]
})

df = pd.concat([df, New_Data],ignore_index = True)
print("\n Final Data Frame")
print(df)
