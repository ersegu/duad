
def find_character(mystring,character):
    char_counter = 0
    for char in mystring:
        if char == character:
            char_counter += 1
    return char_counter
   


text = input("Insert a text:\n").lower()
char_to_find = input("Insert the character to find:\n").lower()

print("The character has been found",find_character(text,char_to_find),"times")



