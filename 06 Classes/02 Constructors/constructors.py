class Person:
    def __init__(self, name):
        self._name = name

    def eating(self):
        print(f"{self._name} is eating!")

p = Person("Bob")
p.eating()
print(p)