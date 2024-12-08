fruits = ("apple", "pear", "orange")
days = ("Mon", "Tue", "Wed")

for i, fruit in enumerate(fruits):
    print(i, fruit)

for fruit, day in zip(fruits, days):
    print(fruit, day)