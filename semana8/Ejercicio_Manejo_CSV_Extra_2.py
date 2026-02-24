
import csv


def search_games_by_esrb(file_path,esrb):
    found_items = []
    game = {}
    try:
        with open(file_path) as csv_file:
            reader = csv.reader(csv_file,dialect='excel')
            headers = next(reader)
            for row in reader:
                for index,item in enumerate(row):
                    game[headers[index]] = item
                if game['classification'].lower() == esrb: 
                    found_items.append(game)
                game = {}
    except (FileNotFoundError, PermissionError, OSError,UnicodeDecodeError,TypeError,ValueError,csv.Error,IndexError, KeyError) as ex:
        print(f"Search has failed: {ex}")
    return found_items


def main():
    try:
        esrb = input("Enter the ESRB Classification to search\n")
        games = search_games_by_esrb('games.csv',esrb.lower())
        for game in games:
            print(game)
    except (TypeError, ValueError) as ex:
        print(f"Unable to perform operation: {ex}")
    except Exception as ex:
        print(f"There has been an error: {ex}")


main()