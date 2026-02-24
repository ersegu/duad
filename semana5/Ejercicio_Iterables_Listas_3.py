# Cree un programa que intercambie el primer y ultimo elemento de una lista. 
# Debe funcionar con listas de cualquier tamaño.
# Ejemplos:
# my_list = [4, 3, 6, 1, 7]`→ [7, 3, 6, 1, 4]


my_list = [4, 3, 6, 1, 7]

print("Before: ", my_list)

first_element = my_list.pop(0)
last_element = my_list.pop(len(my_list)-1)

my_list.insert(0,last_element)
my_list.append(first_element)

print("After: ", my_list)

