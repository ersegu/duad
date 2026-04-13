
class Employee:
    __name: str
    __salary: float

    def __init__(self, name:str, salary:float):
        self.name = name
        self.salary = salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,salary):
        if salary < 0:
            raise ValueError ("Salary cannot be a negative value")
            
        self.__salary = salary


    def promote(self, percentage):
        __increase = self.salary * (percentage / 100)
        self.salary = self.salary + __increase


try:
    employee = Employee("Erson", 100000)
except ValueError as ex:
    print(ex)

print (employee.name)
print(employee.salary)

employee.promote(10)
print(employee.salary)




