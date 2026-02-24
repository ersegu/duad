
import json


def group_pokemon_by_type(file_path):
    pokemons = []
    grouped_pokemons = {}
    new_pokemon = {}
    try:
        with open(file_path) as json_file:
            pokemons = json.load(json_file)
            for pokemon in pokemons:
                for p_type in pokemon['type']:
                    if p_type not in grouped_pokemons:
                        grouped_pokemons[p_type] = []
                    p_name = pokemon['name']['english']
                    p_level = pokemon['level']
                    new_pokemon['name'] = p_name
                    new_pokemon['level'] = p_level
                    grouped_pokemons[p_type].append(new_pokemon)
                    new_pokemon = {}
        calculate_average(grouped_pokemons)
    except (AttributeError, ValueError, TypeError, KeyError, IndexError, json.JSONDecodeError, FileNotFoundError, PermissionError, OSError) as ex:
        print(f"Unable to group pokemons by type: {ex}")
    return grouped_pokemons


def calculate_average(grouped_pokemons):
    average = 0
    counter = 0
    try:
        for type, pokemons in grouped_pokemons.items():
            for pokemon in pokemons:
                average += pokemon['level']
                counter += 1
            print(f"Type: {type} --> Level Average: {average/counter}")
            average = 0
            counter = 0
    except (AttributeError, ValueError, TypeError, ArithmeticError, KeyError, IndexError) as ex:
        print(f"Unable to calculate the Type level average: {ex}")


group_pokemon_by_type('pokemon.json')