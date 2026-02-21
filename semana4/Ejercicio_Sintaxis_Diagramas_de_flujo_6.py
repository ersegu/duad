# Cree un diagrama de flujo que le pida 100 números al usuario
# y muestre el higher de todos.
    # *Ejemplos*:
        # 4, 76, 43, 6, 8 → 76

higher = 0

for i in range(100):
    number = int(input("Enter a number:\n"))
    if(number > higher):
        higher = number

print("The higher number is: ", higher)