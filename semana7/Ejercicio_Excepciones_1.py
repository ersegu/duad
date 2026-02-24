



def menu(current_number):
    operation = 0
    try:
        operation = int(input("""
        Specify the operation to perform.\n
        Use 1 - For addition.\n
        Use 2 - For subtraction.\n
        Use 3 - For multiplication.\n
        Use 4 - For division.\n
        Use 5 - To exit.\n
        """))
        if operation < 1 or operation > 5:
            raise ValueError
        if operation == 5:
                exit()
        
        number = 0
        try:
            number = float(input("Enter a number to use in the operation:\n"))

            if operation == 1:
                current_number = addition(current_number,number)
                print(f"{current_number}\n")
            if operation == 2:
                current_number = subtraction(current_number,number)
                print(f"{current_number}\n")
            if operation == 3:
                current_number = multiplication(current_number,number)
                print(f"{current_number}\n")
            if operation == 4:
                current_number = division(current_number,number)
                print(f"{current_number}\n")
        except ValueError as ex:
            print("Please enter a valid number")

    except ValueError as ex:
        print("Please specify a valid operation", ex)
    
    return current_number


def addition(current_number,new_number):
    try:
        current_number += new_number
    except ArithmeticError as ex:
        print("Arithmetic Error encountered during the operation: ", ex)
    except FloatingPointError as ex:
        print("Floating Point error encountered during the operation: ", ex)
    except OverflowError as ex:
        print("Overflow Error encountered during the operation: ", ex)
    
    return current_number


def subtraction(current_number,new_number):
    try:
        current_number -= new_number
    except ArithmeticError as ex:
        print("Arithmetic Error encountered during the operation: ", ex)
    except FloatingPointError as ex:
        print("Floating Point error encountered during the operation: ", ex)
    except OverflowError as ex:
        print("Overflow Error encountered during the operation: ", ex)

    return current_number


def multiplication(current_number,new_number):
    try:
        current_number *= new_number
    except ArithmeticError as ex:
        print("Arithmetic Error encountered during the operation: ", ex)
    except FloatingPointError as ex:
        print("Floating Point error encountered during the operation: ", ex)
    except OverflowError as ex:
        print("Overflow Error encountered during the operation: ", ex)
    
    return current_number


def division(current_number,new_number):
    try:
        current_number /= new_number
    except ZeroDivisionError:
        print("Cannot perform division by zero.")
    except ArithmeticError as ex:
        print("Arithmetic Error encountered during the operation: ", ex)
    except FloatingPointError as ex:
        print("Floating Point error encountered during the operation: ", ex)
    except OverflowError as ex:
        print("Overflow Error encountered during the operation: ", ex)
    
    return current_number


def main():
    current_number = 0
    while True:
        try:
            current_number = menu(current_number)
        except Exception as ex:
            print("There has been an error: ", ex)
        except KeyboardInterrupt:
            exit()

main()