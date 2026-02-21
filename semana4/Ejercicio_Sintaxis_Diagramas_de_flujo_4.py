# Cree un diagrama de flujo que le pida un number al usuario 
# y muestre “*Fizz*” si es divisible entre 3, 
# “*Buzz*” si es divisible entre 5, 
# y “*FizzBuzz*” si es divisible entre ambos.
    # *Ejemplos*:
        # 33 → Fizz
        # 25 → Buzz
        # 30 → FizzBuzz


number = int(input("Enter a number:\n"))
if(number %3 == 0 and number %5 == 0):
    print("FizzBuzz")
elif(number %3 == 0):
    print("Fizz")
elif(number %5 == 0):
    print("Buzz")


