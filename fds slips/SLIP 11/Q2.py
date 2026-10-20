import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')

frequency = df['Species'].value_counts()

plt.figure(figsize=(7, 5))
plt.bar(frequency.index, frequency.values,
        color=['red', 'green', 'blue'], edgecolor='black')

plt.title("Frequency of Iris Species")
plt.xlabel("Species")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(7, 5))
plt.hist(frequency.values, bins=5,
        color='orange', edgecolor='black')

plt.title("Histogram of Iris Species Frequencies")
plt.xlabel("Frequency")
plt.ylabel("Number of Species")
plt.show()

print("Frequency of Iris Species:")
print(frequency)