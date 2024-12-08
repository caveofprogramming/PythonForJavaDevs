fruits = ["apple", "orange", "banana", "grape", "pear"]

fruits = filter(lambda s: "e" in s, fruits)

print(list(fruits))