#Ejercicio 2
#Cree un programa que le pida al usuario su nombre, apellido, y edad, 
# y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, 
# adulto, o adulto mayor.
#https://www.significados.com/etapas-del-desarrollo-humano/

name = input("Insert your name\n")
last_name = input("Inset your last name\n")
age = int(input("Insert your age\n"))

if (age<=6):
    print(name + " " + last_name + " is a : baby")
elif(age<=12):
    print(name + " " + last_name + " is a: child")
elif(age<=15):
    print(name + " " + last_name + " is a: pre-teenager")
elif(age<=20):
    print(name + " " + last_name + " is a : teenager")
elif(age<=40):
    print(name + " " + last_name + " is a: young adult")
elif(age<=60):
    print(name + " " + last_name + " is an: adult")
else:
    print(name + " " + last_name + " is a: senior adult")