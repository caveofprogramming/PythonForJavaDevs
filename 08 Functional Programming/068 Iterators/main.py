class PowersOfTwo:
    def __iter__(self):
        self._value = 1
        return self

    def __next__(self):
        self._value *= 2

        if self._value > 20:
            raise StopIteration

        return self._value

for i in PowersOfTwo():
    print(i)