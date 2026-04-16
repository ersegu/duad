

class Vehicle:
    def __init__(self, brand:str, year:int):
        self._brand = brand
        self._year = year
    
    def get_info(self):
        return f"{self._brand} ({self._year})"


class Car(Vehicle):
    def __init__(self,brand:str, year:int, doors:int):
        self._brand = brand
        self._year = year
        self._doors = doors
    
    def get_info(self):
        return f"{self._brand} ({self._year}) - {self._doors} doors"

class Motorcycle(Vehicle):
    def __init__(self,brand:str, year:int, type:str):
        self._brand = brand
        self._year = year
        self._type = type
    
    def get_info(self):
        return f"{self._brand} ({self._year}) - Type: {self._type}"


vehicle1 = Car("Toyota",2024,4)
vehicle2 = Motorcycle("Yamaha",2023,"Sport")
vehicle3 = Vehicle("Honda",2023)

print(vehicle1.get_info())
print(vehicle2.get_info())
print(vehicle3.get_info())