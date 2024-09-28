numbers = [0, 1, 2, 3, 4, 5, 6]

numbers.remove(4)
print(numbers)

value = numbers.pop(1)
print(value, numbers)

del numbers[2]
print(numbers)

numbers.clear()
print(numbers)