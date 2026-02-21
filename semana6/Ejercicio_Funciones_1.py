
def print_first_function():
    print("This is the first Function")
    print("This is the first function calling the second function: ")
    print_second_function()


def print_second_function():
    print("This is the second function")


print_first_function()
print_second_function()