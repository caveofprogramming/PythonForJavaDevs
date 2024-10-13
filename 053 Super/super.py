class Machine:
    def __init__(self):
        print("Machine constructor")

class Car(Machine):
    def __init__(self):
        super().__init__()
        print("Car constructor")

c = Car()
