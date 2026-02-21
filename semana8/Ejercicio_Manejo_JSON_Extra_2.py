
import json


def search_pokemon_by_type(file_path, type):
    pokemons = []
    found_pokemons = []
    try:
        with open(file_path) as json_file:
            pokemons = json.loads(json_file.read())
            for pokemon in pokemons:
                for p_type in pokemon['type']:
                    if p_type.lower() == type.lower():
                        found_pokemons.append(pokemon)
    except (json.JSONDecodeError, FileNotFoundError, PermissionError, ValueError, TypeError) as ex:
        print(f"There has been an error: {ex}")
    return found_pokemons


def main():
    try:
        type = input("Insert the pokemon to search (water, fire, grass, etc.)\n")
        pokemons = search_pokemon_by_type('pokemon.json',type)
        print(f"The pokemons of type {type} are:")
        for pokemon in pokemons:
            print(pokemon['name']['english'])
    except (TypeError, ValueError,AttributeError,KeyError) as ex:
        print(f"Unable to perform Search Operation: {ex}")
    except Exception as ex:
        print(f"An error has occurred: {ex}") 


main()