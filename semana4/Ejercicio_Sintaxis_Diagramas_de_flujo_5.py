#Cree un diagrama de flujo que le pida 100 números al usuario y 
# muestre la suma de todos.


sum = 0
for i in range(100):
    number = int(input("Enter a number:\n"))
    sum += number

print("The sum of all numbers is: ",sum)


