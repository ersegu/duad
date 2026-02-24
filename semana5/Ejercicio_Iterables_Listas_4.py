# Cree un programa que elimine todos los números impares de una lista.
# Ejemplos:
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]


my_list = [1,2,3,4,5,6,7,8,9]
new_list = []
print("Before:",my_list)

for number in my_list:
    if(number %2 !=1):
        new_list.append(number)

print("After:",new_list)



