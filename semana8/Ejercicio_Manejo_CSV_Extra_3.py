
import csv


def count_games_by_genre(file_path):
    game_genre = {}
    try:
        with open(file_path) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                genre = row['genre']
                if genre not in game_genre:
                    game_genre[genre] = 0
                game_genre[genre] += 1
    except (FileNotFoundError, PermissionError, OSError,UnicodeDecodeError,TypeError,ValueError,csv.Error, KeyError) as ex:
        print(f"Search has failed: {ex}")
    return game_genre


def main():
    games_by_genre = {}
    try:
        games_by_genre = count_games_by_genre('games_2.csv')
        print("Found Genres:\n")
        for genre, value in games_by_genre.items():
            print(f"{genre}: {value}")
    except (TypeError, ValueError, KeyError) as ex:
        print(f"Unable to perform operation: {ex}")
    except Exception as ex:
        print(f"There has been an error: {ex}")


main()