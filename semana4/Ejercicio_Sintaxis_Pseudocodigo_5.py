# Cree un algoritmo que le pida al usuario una speed en km/h y la convierta a m/s. Recuerda que `1 km == 1000m` y `1 hora == 60 minutos * 60 segundos`.
    #*Ejemplos*:
        #73 → 20.27
        #50 → 13.88
        #120 → 33.33

speed = int(input("Enter the speed in km/h:\n"))
speed_in_meters = speed * 1000/3600
print("The speed in m/s is: ",speed_in_meters)
