stuff = ("Charles", 7, 8.2, True, False, "Cats")

print(stuff[2])
# stuff[2] = "Leaf"

name, value1, value2, bool1, bool2, animal = stuff
print(name, value1, value2, bool1, bool2, animal)

person, number1, number2, *other = stuff
print(person, number1, number2, other)

print(type(other))

animals = ("cat",)
print(animals)