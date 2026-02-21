

def sort_songs (file_path):
    song_list = []
    try:
        with open(file_path) as file:
            for song in file.readlines():
                song_list.append(song)
        song_list.sort()
        write_to_file(song_list)
    except FileNotFoundError as ex:
        print(f"Specified file does not exist. Please validate the provided path is correct.\n {ex}") 


def write_to_file(sorted_song_list):
    try:
        with open("sorted_songs.txt",'w',encoding='UTF-8') as file:
            file.writelines(sorted_song_list)
    except UnicodeError as ex:
        print(f"There has been an unicode error. {ex}")


def main():
    try:
        with open("songs.txt") as file:
            print(f"Song list before:\n{file.read()}\n")
        sort_songs("songs.txt")
        with open("sorted_songs.txt") as file:
            print(f"Sorted song list:\n{file.read()}")
    except Exception as ex:
        print(f"There has been an error: {ex}")


main()


