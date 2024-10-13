class Person:
    def __init__(self, name):
        self._name = name

    def eating(self):
        print(f"{self._name} is eating!")

    def __str__(self):
        return f"Hello I am {self._name}"
    
    def __repr__(self):
        return f'Person("{self._name}")'
    
class Employee(Person):
    def go_on_holiday(self):
        print("I'm going on holiday!")

p = Person("Bob")
e = Employee("Sue")
e.eating()
e.go_on_holiday()


