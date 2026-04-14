

def is_number(func):
    def wrapper(*args:str):
        for arg in args:
            temp_arg = str(arg)
            if not temp_arg.isdigit():
                raise ValueError (f"Parameter '{arg}' is not a number.")
        func(*args)

    return wrapper


@is_number
def my_function(*args):
    print ("This is a muck function")


try:
    my_function(
        1,2,3,4
    )
except ValueError as ex:
    print(ex)