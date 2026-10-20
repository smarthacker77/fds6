import pandas as pd
import numpy as np

data = {
    "X" :[2,5,8,10],
    "Y" :[3,7,4,12]
}

df = pd.DataFrame(data)
print("\n Orignal DataFrame")
print(df)

point1 = df.loc[0,["X"]].to_numpy(dtype =(float))
point2 = df.loc[1,["Y"]].to_numpy(dtype =(float))

Differnace = point1 - point2

Distance = np.linalg.norm(Differnace)
print("\nPoint1 :-",point1)
print("\nPoint2 :-",point2)
print("\nDifferance :-",Differnace)
print("\nDistance :-",Distance)