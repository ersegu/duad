
def program_logic():
    name = ""
    age = 0
    try:
        name = input("Please enter your name:\n")
        if name.isdigit():
            raise ValueError("The name cannot be a number.")
        try:
            age = int(input("Enter your age:\n"))
        except ValueError as ex:
            print("Enter a valid age. ",ex)
        else:
            print(f"Hello {name}, your age is {age}")
    except ValueError as ex:
        print("Enter a valid name.", ex)


try:
    program_logic()
except Exception as ex:
    print("There has been an error.", ex)