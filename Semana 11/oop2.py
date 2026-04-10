

class Person:
    def __init__ (self, name):
        self.name = name
    
    def __str__(self):
        return self.name

    def __repr__ (self):
        return self.name


class Bus:

    def __init__(self):
        self.passangers = []
        self.max_passangers = 5

    def add_passanger(self,person):
        if (len(self.passangers) >= self.max_passangers):
            print(f"Passanger {person.name} cannot get in the Bus as it is full")
            return
        
        self.passangers.append(person)
        print(f"Passanger {person.name} is now in the bus")
    
    def remove_passanger(self, person):
        if (len(self.passangers) == 0):
            print("Bus is empty")
            return
        
        self.passangers.remove(person)
        print(f"Passenger {person.name} is no longer in the bus")



person_1 = Person("Juan")
person_2 = Person("Pedro")
person_3 = Person("Lucia")
person_4 = Person("Miguel")
person_5 = Person("Hector")
person_6 = Person("Fernando")

my_bus = Bus()
new_bus = Bus()

my_bus.remove_passanger(person_1)

my_bus.add_passanger(person_2)
my_bus.add_passanger(person_3)
my_bus.add_passanger(person_4)
my_bus.add_passanger(person_5)
my_bus.add_passanger(person_6)
new_bus.add_passanger(person_1)

my_bus.remove_passanger(person_3)

print(my_bus.passangers)
print(new_bus.passangers)

