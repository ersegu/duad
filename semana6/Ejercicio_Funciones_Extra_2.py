
def word_finder(word_list,number):
    new_word_list = []
    for word in word_list:
        char_counter = 0
        for char in word:
            char_counter += 1
        if char_counter > number:
            new_word_list.append(word)
    return new_word_list


word_list = ["cielo", "sol", "maravilloso", "día"]
number = int(input("Insert the minimum amount of letters the word should have:\n"))
print(word_finder(word_list,number))





