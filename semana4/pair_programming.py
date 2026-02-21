#Ejercicio 1 
#Dadas las horas trabajadas de una persona y su tarifa por hora
# calcular y mostrar su salario.

horas_trabajadas = int(input("Ingrese sus horas trabajadas\n"))
tarifa_hora = int(input("Ingrese su tarifa por hora\n"))
salario = horas_trabajadas * tarifa_hora
print("Su salario sera de: ",salario)

#Ejercicio 2
#Dado el nombre y apellido de un empleado, y el dominio .com de una empresa
# genere su email usando el formato <nombre>.<apellido>@<dominio_de_empresa>.com.

nombre = input("Ingrese su nombre:\n")
apellido = input("Ingrese su apellido:\n")
empresa = input("Ingrese el nombre de la empresa:\n")
print(f"Su correo es: {nombre}.{apellido}@{empresa}.com")
