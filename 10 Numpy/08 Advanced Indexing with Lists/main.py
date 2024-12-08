import numpy as np

values = np.arange(16).reshape(4, 4)
print(values)
print()

print(values[[0, 2, 2, 3],[0, 0, 2, 1]])