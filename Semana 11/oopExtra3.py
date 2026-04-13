

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"Product: {self.name} Price: ${self.price} Quantity: {self.quantity}"


class Inventory:
    products = []

    def add_product(self,product):
        self.products.append(product)
    
    def show_products(self):
        for product in self.products:
            print(product)
    
    def calculate_inventory_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.quantity * product.price
        return total_value


product1 = Product("Mouse",5000,3)
product2 = Product("Keyboard", 8000, 2)

product_list = Inventory()
product_list.add_product(product1)
product_list.add_product(product2)

product_list.show_products()
print(f"Inventory Value: {product_list.calculate_inventory_value()}")


