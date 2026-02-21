# Cree un programa que reciba una lista de números y 
# calcule el promedio de los valores.
# Luego cree una nueva lista con solo los valores mayores al promedio

my_list = [10, 20, 30, 40, 50]
average = 0

for number in my_list:
    average += number

average = average / len(my_list)

new_list = []
for number in my_list:
    if(number > average):
        new_list.append(number)

print("Average: ",average)
print("New List: ", new_list)



