import numpy as np
import matplotlib.pyplot as plt

d1 = np.random.normal(50, 10, 1000)
d2 = np.random.normal(70, 15, 1000)

plt.hist(d1, bins=20, alpha=0.6, edgecolor='black', label='Dataset 1')
plt.hist(d2, bins=20, alpha=0.6, edgecolor='black', label='Dataset 2')

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Normal Distributions")
plt.legend()
plt.show()