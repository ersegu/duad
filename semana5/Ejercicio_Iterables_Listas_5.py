# Cree un programa que le pida al usuario 10 números, 
# y al final le muestre todos los números que ingresó, 
# seguido del numero ingresado más alto.
# Ejemplos:
# 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

my_list = []
biggest_number = 0

for i in range(10):
    number = int(input("Insert a number:\n"))
    my_list.append(number)
    if(number > biggest_number):
        biggest_number = number

print("The inserted numbers were:\n", my_list)
print("The biggest number was: ", biggest_number)

