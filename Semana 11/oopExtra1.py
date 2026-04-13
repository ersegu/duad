

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

def is_number_valid(number):
    if number < 0:
        raise ValueError("You cannot use negative values.")
    return True

    
try:
    width = float(input("Insert the Rectangle's Width: "))
    height = float(input("Insert the Rectangle's Height: "))

    if (is_number_valid(width)) and (is_number_valid(height)):
        rectangle = Rectangle(width,height)
        print(rectangle.get_area())
        print(rectangle.get_perimeter())

except (TypeError, AttributeError, ValueError) as ex:
    print(f"An error has occurred {ex}")
    



