

class Person:
    def __init__ (self, name):
        self.name = name


class Bus:
    passangers = []
    max_passangers = 5

    def add_passanger(self,person):
        if (len(self.passangers) >= self.max_passangers):
            print(f"Passanger {person.name} cannot get in the Bus as it is full")
            return
        
        self.passangers.append(person)
        print(f"Passanger {person.name} is now in the buss")
    
    def remove_passanger(self, person):
        if (len(self.passangers) == 0):
            print("Bus is empty")
            return
        
        self.passangers.remove(person)
        print(f"Passenger {person.name} is no longer in the buss")



person_1 = Person("Juan")
person_2 = Person("Pedro")
person_3 = Person("Lucia")
person_4 = Person("Miguel")
person_5 = Person("Hector")
person_6 = Person("Fernando")

my_bus = Bus()

my_bus.remove_passanger(person_1)

my_bus.add_passanger(person_2)
my_bus.add_passanger(person_3)
my_bus.add_passanger(person_4)
my_bus.add_passanger(person_5)
my_bus.add_passanger(person_6)
my_bus.add_passanger(person_1)

my_bus.remove_passanger(person_3)
