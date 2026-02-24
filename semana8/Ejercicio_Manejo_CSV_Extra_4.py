
import csv


def search_games_by_developer(file_path,developer):
    found_games = []
    try:
        with open(file_path) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if developer == row['developer'].lower():
                    found_games.append(row)
    except (FileNotFoundError, PermissionError, OSError,UnicodeDecodeError,TypeError,ValueError,csv.Error, KeyError) as ex:
        print(f"Unable to perform the search: {ex}")
    return found_games


def main():
    try:
        developer = input("Enter the developer to search\n")
        games = search_games_by_developer('games_2.csv',developer.lower())
        print(f"Games developed by {developer.title()}")
        for game in games:
            print(f"- {game['name']} (Classification: {game['classification']}, Genre: {game['genre']})")
    except (TypeError, ValueError) as ex:
        print(f"Unable to perform operation: {ex}")
    except Exception as ex:
        print(f"There has been an error: {ex}")


main()