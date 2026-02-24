

def convert_to_int(list):
    print("Result:")
    for item in list:
        try:
            print(f"'{item}' converted to: {int(item)}")
        except ValueError:
            print(f"Unable to convert the element: '{item}'")


try:
    convert_to_int(['4','hola','10','5.2'])
except Exception as ex:
    print(f"There has been an error: {ex}")
