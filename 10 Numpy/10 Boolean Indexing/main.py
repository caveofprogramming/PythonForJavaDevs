import numpy as np

values = np.arange(16).reshape(4, 4)
print(values)
print()

print(values[values % 5 == 0])

rng = np.random.default_rng()

numbers = rng.standard_normal(50)
print(numbers.mean())

positives = numbers[numbers < 0]
print(positives.mean())