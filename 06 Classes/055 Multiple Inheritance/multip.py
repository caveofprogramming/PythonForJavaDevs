class Car:
    def start(self):
        print("Car starting")

class Alarm:
    def on(self):
        print("Alarm on")

class SafeCar(Car,Alarm):
    pass

s = SafeCar()
s.start()
s.on()