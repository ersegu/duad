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
