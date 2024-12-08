data1 = b'Hello'
print(data1)
print(type(data1))

data2 = bytearray([0xFF, 1, 2, 3, 4])

with open('test1.bin', 'wb') as file:
    file.write(data1)

with open('test2.bin', 'wb') as file:
    file.write(data2)