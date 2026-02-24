# **Cree un programa que cuente cuántas veces aparece un número específico 
# en una lista. Pida al usuario una lista de números y otro número a buscar**

my_list = []

counter = int(input("Indicate the amount of numbers to add to the list:\n"))

while(counter > 0):
    number = int(input("Add a number to the list:\n"))
    my_list.append(number)
    counter -= 1

counter = 0
number_to_search = int(input("Insert the number you want to look for:\n"))

for number in my_list:
    if(number == number_to_search):
        counter += 1

print("The number ",number_to_search," appears ",counter," time(s)")

