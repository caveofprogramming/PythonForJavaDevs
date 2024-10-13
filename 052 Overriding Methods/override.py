class Animal:
    def speak(self):
        print("I'm an animal")

class Cat(Animal):
    def speak(self):
        print("Meeouw")

cat = Cat()
cat.speak()