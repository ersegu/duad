# Cree un programa que le pida al usuario ingresar 5 palabras.
# Luego muestre una nueva lista con solo aquellas palabras que 
# tengan más de 4 letras


word_list = []

for i in range(5):
    new_word = input("Type a Word\n")
    word_list.append(new_word)

new_word_list = []
for word in word_list:
    char_counter = 0
    for char in word:
        char_counter += 1
    if(char_counter > 4):
        new_word_list.append(word)

print("List of typed words: ",word_list)
print("New list of words: ", new_word_list)

