import numpy as np

values = np.arange(0, 16, 1).reshape(4, 4)
print(values)
print()
print(values[::2])
print()
print(values[::2,1:3])
