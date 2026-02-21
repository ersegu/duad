# Cree un diagrama de flujo que le pida 5 números al usuario y muestre el higher.
    # *Ejemplos*:
        # 4, 76, 43, 6, 8 → 76
        # 1, 2, 3, 6, 7 → 7
        # 2132, 4355, 1132, 2323, 1214 → 4355

higher = 0

for i in range(5):
    number = int(input("Enter a number:\n"))
    if(number > higher):
        higher = number

print("The higher number is: ", higher)



