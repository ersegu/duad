# Cree un diagrama de flujo que pida 3 números al usuario. 
# Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “*Correcto*”. 
# Sino, mostrar “*incorrecto*”.
    # *Ejemplos*:
        # 23, 30, 768 → Correcto (hay un 30)
        # 10, 15, 5 → Correcto (10 + 15 + 5 = 30)
        # 35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)


first_number = int(input("Enter the first number:\n"))
second_number = int(input("Enter the second number:\n"))
third_number = int(input("Enter the third number:\n"))

if(first_number == 30 or second_number == 30 or third_number == 30 or first_number + second_number + third_number == 30):
    print("Correct!")
else:
    print("Incorrect")