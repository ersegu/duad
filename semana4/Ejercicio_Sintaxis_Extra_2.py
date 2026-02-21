# **Tabla de multiplicar personalizada**
    # - Pida al usuario un número del 1 al 10
    # - Muestre su tabla de multiplicar del 1 al 12
    # - Ejemplo:
        # - Entrada: 
            #"Ingrese un número:" 7
        # - Salida:
            # 7 x 1 = 7
            # 7 x 2 = 14
            # ...
            # 7 x 12 = 84

number = int(input("Enter a number from 1 to 10:\n"))

for i in range(12):
    print(number, " x ",i+1," = ",number * (i+1))
