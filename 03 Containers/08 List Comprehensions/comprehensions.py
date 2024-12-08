numbers = [i for i in range(0, 5)]
print(numbers)

numbers = [i**2 for i in range(0, 5)]
print(numbers)

animals1 = ["cat", "mouse", "dog", "badger"]

animals2 = [animal for animal in animals1]
print(animals2)

lengths = [len(animal) for animal in animals1]
print(lengths)
