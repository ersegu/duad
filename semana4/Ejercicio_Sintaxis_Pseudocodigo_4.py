# Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas (`first` y `second`) y los ordene de menor a mayor en dichas variables.
    #Ejemplos:
        #A: 56, B: 32 → A: 32, B: 56
        #A: 24, B: 76 → A: 24, B: 76
        #A: 45, B: 12 → A: 12, B: 45

wildcard = 0

first = int(input("Enter the first number:\n"))
second = int(input("Enter the second number:\n"))

if(first > second):
    wildcard = first
    first = second
    second = wildcard

print(first, second)