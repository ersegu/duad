

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "It makes a sound"

class Dog(Animal):
    def speak(self):
        return "Guau"

class Cat(Animal):
    def speak(self):
        return "Miau"



dog = Dog("Apollo")
cat = Cat("Michi")

print(dog.speak())
print(cat.speak())

