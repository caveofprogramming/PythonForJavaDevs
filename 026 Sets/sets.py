numbers = {1, 3, 6, 4}
print(numbers)

for x in numbers:
    print(x)

print(3 in numbers)

numbers.add(7)
print(numbers)

numbers.update([9, 8])
print(numbers)

numbers.remove(8)
print(numbers)

numbers.discard(3)
print(numbers)

print(set([1, 2, 3]))
print({n for n in range(5, 8)})