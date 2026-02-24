

def add_values(list):
    total = 0
    for item in list:
        try:
            total += float(item)
            print(f"{item} added successfully.")
        except ValueError:
            print(f"Invalid element: {item}")

    print(f"Total sum: {total}")


my_list = ['10', 'manzana', '5.5', '3', 'n/a']

try:
    add_values(my_list)
except Exception as ex:
    print(f"An error has occurred. Apologies! {ex}")