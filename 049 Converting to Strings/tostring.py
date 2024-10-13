class Person:
    def __init__(self, name):
        self._name = name

    def eating(self):
        print(f"{self._name} is eating!")

    def __str__(self):
        return f"Hello I am {self._name}"

p = Person("Bob")
p.eating()
print(p)

text = str(p)
print(text)