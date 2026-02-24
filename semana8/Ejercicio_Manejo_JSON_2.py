
import json

def add_new_pokemon(file_path,pokemon):
    pokemons = []
    try:
        with open(file_path) as json_file:
            pokemons = json.load(json_file)
        pokemons.append(pokemon)
        pokemons = json.dumps(pokemons,indent=5)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(pokemons) 
    except (JSONDecodeError, FileNotFoundError, PermissionError, OSError, ValueError, AttributeError, TypeError, UnicodeError) as ex:
        print(f"An error has occurred: {ex}")    

def main():
    pokemon = {}
    p_types = []
    try:
        name = input("Insert the new Pokemon name in English\n")
        while True:
            type = input("Specify the pokemon type (Electric, Fire, Water, etc)\n")
            p_types.append(type)
            break_loop = input("Do you want to add another type to this pokemon? Enter 'Yes' or 'No'\n")
            if break_loop.lower() == 'no':
                break 
        level = int(input("Enter the pokemon's level\n"))
        hp = int(input("Enter the pokemon's HP stat\n"))
        attack = int(input("Enter the pokemon's Attack stat\n"))
        defense = int(input("Enter the pokemon's Defense stat\n"))
        sp_attack = int(input("Enter the pokemon's Sp.Attack stat\n"))
        sp_defense = int(input("Enter the pokemon's Sp.Defense stat\n"))
        speed = int(input("Enter the pokemon's Speed stat\n"))
        pokemon['name'] = {'english':name}
        pokemon['type'] = p_types
        pokemon['level'] = level
        pokemon['base'] = {'HP':hp,'Attack':attack,'Defense':defense,'Sp. Attack':sp_attack,'Sp. Defense':sp_defense,'Speed':speed}
        add_new_pokemon('pokemon.json',pokemon)
    except (ValueError, TypeError, AttributeError, KeyError) as ex:
        print(f"Unable to add Pokemon: {ex}")


main()