

import json


def print_pokemon_info(file_path):
    pokemons = []
    try:
        with open(file_path) as json_file:
            pokemons = json.load(json_file)
            for pokemon in pokemons:
                print(f"""
                Name: {pokemon['name']['english']}
                Type: {pokemon['type']}
                Level: {pokemon['level']}
                HP: {pokemon['base']['HP']}
                Attack: {pokemon['base']['Attack']}
                Defense: {pokemon['base']['Defense']}
                Sp. Attack: {pokemon['base']['Sp. Attack']}
                Sp. Defense: {pokemon['base']['Sp. Defense']}
                Speed: {pokemon['base']['Speed']}
                """)
    except (json.JSONDecodeError, FileNotFoundError, PermissionError, OSError, KeyError, ValueError, TypeError) as ex:
        print(f"There has been an error: {ex}")


print_pokemon_info('pokemon.json')
