# Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.
    # *Ejemplos*:
        # 1, 1, 1, 2, 2, 2 → 50% mujeres y 50% hombres
        # 1, 1, 2, 2, 2, 2 → 33.3% mujeres y 66.6% hombres
        # 1, 1, 1, 1, 1, 2 → 83.3% mujeres y 16.6% hombres

counter = 0
women_counter = 0
man_counter = 0

while(counter <6):
    user_gender = int(input("Enter the person's gender. Use 1 if its a women or 2 if its a man:\n"))
    if(user_gender == 1):
        women_counter += 1
    else:
        man_counter += 1
    counter += 1

male_percentage = man_counter * 100 / 6
female_percentage = women_counter * 100 / 6

print("The percentage of male is: ",male_percentage, "%")
print("The percentage of female is: ",female_percentage, "%")

