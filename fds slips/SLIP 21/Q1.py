import numpy as np

marks = np.array([85, 72, 45, 90, 35, 60, 55, 28, 78, 40])

low = medium = high = 0

for m in marks:
    if m < 40:
        low += 1
    elif m < 70:
        medium += 1
    else:
        high += 1

print("Below 40:", low)
print("40 to 69:", medium)
print("70 and above:", high)