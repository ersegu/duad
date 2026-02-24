# Cree un pseudocódigo que le pida un `tiempo en segundos` al usuario 
# y calcule si es menor o mayor a 10 minutos. 
# Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. 
# Si es mayor, muestre “*Mayor*”. 
# Si es exactamente igual, muestre “*Igual*”.
    # *Ejemplos*:
        # 1040 → Mayor
        # 140 → 460
        # 600 → Igual
        # 599 → 1


time_remaining = 0

time_in_seconds = int(input("Enter the time in seconds\n"))
if(time_in_seconds < 600):
    time_remaining = 600 - time_in_seconds
    print("To reach 10 min, ",time_remaining, " seconds are needed.")
elif(time_in_seconds > 600):
    print("Higher")
else:
    print("Same")