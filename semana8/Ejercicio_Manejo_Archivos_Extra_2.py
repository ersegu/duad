


def count_words (file_path):
    word_counter = 0
    word_list = []
    try:
        with open(file_path) as file:
            for line in file.readlines():
                word_list.extend(line.split())
            for item in word_list:
                word_counter += 1
        return word_counter
    except FileNotFoundError as ex:
        print(f"Specified file does not exist. Please validate the provided path is correct.\n {ex}")

def main():
    try:
        print(f"This file contain(s) {count_words("words.txt")} word(s)")
    except Exception as ex:
        print(f"There has been an error: {ex}")


main()