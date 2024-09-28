fruits = ["apple", "orange", "grape"]

print(id(fruits))
fruits += ["melon"]
print(id(fruits))

print(fruits)

fruits[0] = "strawberry"
print(fruits)

fruits.append("pear")
print(fruits)

fruits.extend(["blueberry"])
print(fruits)

fruits.insert(2, "kiwi")
print(fruits)

fruits_tuple = tuple(fruits)
print(fruits_tuple)

fruits_list = list(fruits_tuple)
print(fruits_list)