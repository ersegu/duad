"""
Multiple Inheritance in Python allows a class to inherit Methods or Attributes from multiple parent classes at the same time.
This tend to be useful when you want to leverage functionalities or reuse code from unrelated classes.
However, using multiple inheritance represent certain risks such as multiple parents defining the same method this is known as the Diamond Problem. 
For this Python uses the Method Resolution Order (MRO) to determine the order of execution. 
MRO determines the order in which classes are searched. It first searches the current class, then the parent classes from left to right. Each class is searched once.

An example of Multiple Inheritance can be seen below:
"""

class A:
    def __init__(self):
        print("I'm from Class A")
    def a(self):
        print("This method was inherited from Class A")

class B:
    def __init__(self):
        print("I'm from Class B")
    def b(self):
        print("This method was inherited from Class B")

class C(B,A):
    def c(self):
        print("This method is from Class C")


object_c = C()
object_c.a()
object_c.b()
object_c.c()

"""
Expected Output:
/bin/python "/home/firegrizzly/Documents/Lyfter/duad/Semana 12/pilaresOOP3.py"
I'm from Class B
This method was inherited from Class A
This method was inherited from Class B
This method is from Class C
"""
