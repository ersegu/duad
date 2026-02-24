# Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, 
# cree un diccionario que acumule el total por categoría.

#Input: 

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

categories = ["Electrónica","Muebles"]
total_by_category = {}   

for i in range(len(categories)):
    total_category = 0
    for product in products:
        if(product["category"]== categories[i]):
            total_category += product["price"]
    total_by_category[categories[i]] = total_category


print(total_by_category)