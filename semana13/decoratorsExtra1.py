
def repeat_twice(func):
    def wrapper(name):
        func(name)
        func(name)
    return wrapper


@repeat_twice
def print_hello(name):
    print(f"Hello, {name}")


print_hello("Erson")
