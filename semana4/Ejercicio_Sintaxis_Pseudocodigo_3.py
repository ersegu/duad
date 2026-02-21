# Cree un algoritmo que le pida un number al usuario, 
# y realice una suma de cada number del 1 hasta ese número ingresado. 
# Luego muestre el resultado de la suma.
    #5 → 15 (1 + 2 + 3 + 4 + 5)
    #3 → 6 (1 + 2 + 3)
    #12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

counter = 1
total_sum = 0

number = int(input("Enter a number:\n"))
while(counter<=number):
    total_sum = total_sum + counter
    counter = counter + 1
print("The result of the sum is: ",total_sum)

