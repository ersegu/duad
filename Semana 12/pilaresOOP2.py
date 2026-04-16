
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter

    def calculate_area(self):
        area =  3.14 * (self.radius ** 2)
        return area

class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def calculate_perimeter(self):
        perimeter = self.side * 4
        return perimeter
    def calculate_area(self):
        area = self.side ** 2
        return area
    

class Rectangle(Shape):
    def __init__ (self, lenght, width ):
        self.lenght = lenght
        self.width = width

    def calculate_perimeter(self):
        perimeter = (self.lenght * 2) + (self.width * 2)
        return perimeter
    
    def calculate_area(self):
        area = self.lenght * self.width
        return area


circle = Circle(5)
Square = Square(3)
rectangle = Rectangle(4,2)

print(circle.calculate_perimeter())
print(circle.calculate_area())

print(Square.calculate_perimeter())
print(Square.calculate_area())

print(rectangle.calculate_perimeter())
print(rectangle.calculate_area())


