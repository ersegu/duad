#Ejercicio 3
#Cree un programa con un numero secreto del 1 al 10. 
# El programa no debe cerrarse hasta que el usuario adivine el numero.
#Investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
# https://docs.python.org/es/3/library/random.html


import random

secret_number = random.randint(1,10)
user_number = 0

while(user_number != secret_number): 
    user_number = int(input("Guess the Secret Number\n"))
    if(user_number==secret_number):
        print("Congratulations! You've guessed the secret number!\n" + "Secret Number: ", user_number)
    else:
        print("You missed, Try again!")
