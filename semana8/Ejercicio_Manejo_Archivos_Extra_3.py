

def read_file(file_path):
    text = []
    try:
        with open(file_path) as file:
            for line in file.readlines():
                text.append(line.upper())

        write_to_file(text)
    except FileNotFoundError as ex:
        print(f"Specified file does not exist. Please validate the provided path is correct.\n {ex}")


def write_to_file(text):
    try:
        with open("new_file.txt",'a',encoding='UTF-8') as file:
            file.writelines(text)
    except UnicodeError as ex:
        print(f"There has been an unicode error. {ex}")


def main():
    try:
        with open("old_file.txt") as file:
            print(f"Before:\n{file.read()}\n")
        read_file("old_file.txt")
        with open("new_file.txt") as file:
            print(f"After:\n{file.read()}")
    except FileNotFoundError as ex: 
        print(f"Specified file does not exist. Please validate the provided path is correct.\n {ex}") 
    except Exception as ex:
        print(f"There has been an error: {ex}")


main()