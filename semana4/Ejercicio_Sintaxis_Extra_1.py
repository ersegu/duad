# **Convertidor de unidades de temperatura**
    # - Pida al usuario ingresar una temperatura en Celsius
    # - Conviértala a Fahrenheit y Kelvin
    # - Muestre los tres valores
    # - Ejemplo:
        # - Entrada: "Ingrese temperatura en Celsius:" 25
        # - Salida:
            # Fahrenheit: 77.0
            # Kelvin: 298.15

# C = (F - 32) / 1.8
# C * 1.8 = F - 32
# (C * 1.8) + 32 = F

# F = (C*1.8) + 32
# K = C + 273.15

temperature_in_celsius = float(input("Enter the temperature in Celsius:\n"))
temperature_in_fahrenheit = (temperature_in_celsius * 1.8) + 32
temperature_in_kelvin = temperature_in_celsius + 273.15

print("Temperature in Celcius: ", temperature_in_celsius, "\nTemperature in Fahrenheit: ", temperature_in_fahrenheit, "\nTemperature in Kelvin: ", temperature_in_kelvin)
