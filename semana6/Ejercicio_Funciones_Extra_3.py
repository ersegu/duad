
def count_vowels(mystring):
    vowel_counter = 0
    for char in mystring:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vowel_counter += 1
    return vowel_counter


print(count_vowels("Hello World".lower()))

