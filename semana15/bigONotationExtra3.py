

def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict: 
            print(f"{key1}-{key2}")


"""
¿Cuál es la complejidad temporal?
R>> So it has a complexity of O(N^2) due to the 2 for loops.
¿Cuanto dura si hay 1 millón de claves?
R>> A lot of time, probably days depending on where you execute it (hardware) as 1Million Keys, that would be 1Million * 1Million = 1,000,000,000,000
"""