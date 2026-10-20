import numpy as np

data = np.array([3, 4, 5, 6, 7])

normalized = data / np.linalg.norm(data)

print("Original Data:", data)
print("Normalized Data:", normalized)