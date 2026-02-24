#Ejercicio 4
#Cree un programa que le pida tres números al usuario y muestre el mayor.
#https://ellibrodepython.com/for-python

biggest_number = 0

for i in range(3):
    number = int(input("Provide a number:\n"))
    if (number > biggest_number):
        biggest_number = number
    
print("The biggest number is: ",biggest_number)

