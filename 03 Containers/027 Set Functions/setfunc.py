numbers1 = {2, 4, 6, 7, 8, 9}
numbers2 = {2, 4, 6, 1, 3, 5}

print(numbers1.union(numbers2))
print(numbers1.intersection(numbers2))

print(numbers1.difference(numbers2))
print(numbers1 - numbers2)
print(numbers2.difference(numbers1))
print(numbers2 - numbers1)
print(numbers2.symmetric_difference(numbers1))

print({1, 2, 3}.issuperset({1, 2, 3}))
print({1, 2, 3, 4, 5}.issuperset({1, 2, 3}))
print({1, 2, 3}.issuperset({1, 2, 3, 4}))