#Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, 
# y le pida al usuario adivinar ese número. 
# El algoritmo no debe terminar hasta que el usuario adivine el numero.

import random

secret_number = random.randint(1,10)
user_number = 0

while(user_number != secret_number): 
    user_number = int(input("Guess the secret number:\n"))
    if(user_number==secret_number):
        print("Congrats! You've guessed the secret number!\n" + "Secret number: ", user_number)
    else:
        print("Wrong! Try again.")