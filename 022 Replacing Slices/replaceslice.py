numbers = list((0, 1, 2, 3, 4, 5, 6, 7))

numbers[2:4] = (0, 0, 0, 0)
print(numbers)

numbers[2:6] = []
print(numbers)

numbers[1::2] = ["hello", "to", "you"]
print(numbers)