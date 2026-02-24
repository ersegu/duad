

def print_backwards(my_string):
    new_string = ''
    for i in range(len(my_string)-1,-1,-1):
        new_string += my_string[i]

    return new_string


print(print_backwards("Hola Mundo"))

