file = open("test.txt")

#lines = file.readlines()

lines = file.read().splitlines()

print(lines)

file.close()