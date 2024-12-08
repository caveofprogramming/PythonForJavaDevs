import numpy as np

values = np.arange(16).reshape(4,4) * 10

print(values)

view = values[:, 1:3]
print(view)

view *= 0
print(view)

print(values)