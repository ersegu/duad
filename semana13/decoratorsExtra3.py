
from datetime import datetime


def validate_numbers(func):
    def wrapper(*args):
        for arg in args:
            temp_arg = str(arg)
            if not temp_arg.isdigit():
                raise ValueError (f"The argument '{arg}' is not a number.")
        return func(args[0],args[1])
    return wrapper

def log_call(func):
    def wrapper(*args):
        timestamp = datetime.now()
        number1 = args[0]
        number2 = args[1]
        result = func(number1,number2)
        print(f"func:multiply - args: {number1}, {number2} - [{timestamp}] - Result: {result}")
        return result
    return wrapper

@validate_numbers
@log_call
def multiply(number1,number2):
    return number1 * number2


try:
    print(f"Result: {multiply(3,4)}")
except ValueError as ex:
    print(ex)