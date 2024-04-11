# How to use numpy.argsort in Descending order in Python

import numpy as np

arr = np.array([4, 1, 5, 7])

print(arr.argsort())  # 👉️ [1 0 2 3]

# ✅ Using numpy.argsort() in descending order
print((-arr).argsort())  # 👉️ [3 2 0 1]
