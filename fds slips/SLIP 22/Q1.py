import pandas as pd

subjects = ['Python', 'Java', 'DBMS', 'CN', 'AI']
marks = [85, 78, 90, 75, 88]

df = pd.DataFrame({
    'Subject': subjects,
    'Marks': marks
})

print(df)