

def print_parameters(func):
    def wrapper(*args):
        for index, arg in enumerate(args):
            print(f"Argument {index}: {arg}")
        
        result = func(*args)
        
        print(f"Function returned: {result}")
    return wrapper


@print_parameters
def my_function(*args):
    return "This is a muck function"



my_function(
    "hello","testing","my","function",1,2,3,4
)


