
def write_to_file(text):
    try:
        with open("file.txt",'a',encoding='UTF-8') as file:
            file.write(f"{text}\n")
    except UnicodeError as ex:
        print(f"There has been an unicode error. {ex}")


def main():
    text = ""
    try:
        text = input("Insert the text you want to add to the file:\n")
        write_to_file(text)
        with open("file.txt") as file:
            print(f"\nText added successfully.\n{file.read()}")
    except FileNotFoundError as ex: 
        print(f"Specified file does not exist. Please validate the provided path is correct.\n {ex}") 
    except Exception as ex:
        print(f"There has been an error: {ex}")


main()