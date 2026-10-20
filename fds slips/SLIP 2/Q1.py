import pandas as pd

Marks = [67,87,95,98,59,59,86,97]

s = pd.Series(Marks)
print("\nOrignal Series :-")
print(s)

print("\nSum Of Series :-",s.sum())
print("\nAverage Of Series ;-",s.mean())
print("\nMedian Of Series :-",s.median())
print("\nMode Of Series :-",s.mode())
print("\nMaximum Of Series ;-",s.max())
print("\nMinimum Of Series :-",s.min())
print("\nStandard Deviation :-",s.std())