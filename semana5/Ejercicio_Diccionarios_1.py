# Cree un diccionario que guarde la siguiente información sobre un hotel:
    # - nombre
    # - numero_de_estrellas
    # - habitaciones

# - El value del key de habitaciones debe ser una lista, 
# y cada habitación debe tener la siguiente información:
    # - numero
    # - piso
    # - precio_por_noche

hotel = {
    "name": "Mi Hotel",
    "number_of_stars": 4,
    "rooms": [
        {
            "number": 11,
            "floor": 1,
            "price_per_night": 400
        },
        {
            "number":22,
            "floor":2,
            "price_per_night":450
        },
        {
            "number":33,
            "floor":3,
            "price_per_night":500
        },
        {
            "number":44,
            "floor":4,
            "price_per_night":600
        }
    ]
}

print(hotel["rooms"][2])
