# Cree un programa que muestre el valor más pequeño de una lista sin usar min()
# - Use una variable para comparar uno a uno
# - Ejemplo:
#     - Entrada:
#       my_list = [9, 4, 7, 1, 5]
#     - Salida:
#         "El menor valor es 1"


my_list = [9, 4, 7, 1, 5]
lower_number = my_list[0]

for number in my_list:
    if(number < lower_number):
        lower_number = number

print("The lowest number is: ",lower_number)

