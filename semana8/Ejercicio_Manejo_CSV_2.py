
import csv


def request_games():
    game_list = []
    game = {}
    try:
        while True:
            game['name'] = input("Enter the video game's name:\n")
            game['genre'] = input("Enter the video games' genre\n")
            game['developer'] = input("Enter the game's developer\n")
            game['classification'] = input("Enter the game's ESRB classification\n")
            game_list.append(game)
            break_loop = input("Do you want to add another video game?\nPlease enter either 'Yes' or 'No'\n")
            if break_loop.lower() == "no":
                break
            game = {}
    except (TypeError, ValueError, KeyError) as ex:
        print(f"Unable to add game {ex}")
    return game_list
        
def write_to_csv_using_tab(file_path,data,headers):
    try:
        with open(file_path,'w',encoding='utf-8') as file:
            writer = csv.DictWriter(file,headers,dialect='excel-tab')
            writer.writeheader()
            writer.writerows(data)
    except FileNotFoundError as ex:
        print(f"Unable to find specified file. Please check the provided path. {ex}")
    except PermissionError as ex:
        print(f"Unable to write file. Please check permissions. {ex}")
    except OSError as ex:
        print(f"An OS error has occurred. {ex}")
    except csv.Error as ex:
        print(f"Unable to write to file. {ex}")
    except UnicodeEncodeError as ex:
        print(f"Unable to encode the data. {ex}")
    except TypeError as ex:
        print (f"Incorrect type used. {ex}")
    except ValueError as ex:
        print(f"Incorrect value specified. {ex}")
    

def main ():
    try:
        game_list = request_games()
        write_to_csv_using_tab('games_tab.csv',game_list,game_list[0].keys())
    except Exception as ex:
        print(f"There has been an error. {ex}")


main()
#print(csv.list_dialects())
#Used to get the list of dialects available. ['excel', 'excel-tab', 'unix']