import pandas as pd
import numpy as np

df = pd.DataFrame({'X': [2, 4, 6], 'Y': [3, 7, 9]})

p1 = df.iloc[0].values
p2 = df.iloc[1].values

d = p1 - p2

print("Difference Vector:", d)
print("Euclidean Distance:", np.sqrt(np.sum(d**2)))
print("Manhattan Distance:", np.sum(np.abs(d)))