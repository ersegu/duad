#1. Cree un pseudocódigo que le pida un `precio de producto` al usuario, 
# calcule su descuento y muestre el precio final tomando en cuenta que:
    # Si el precio es menor a 100, el descuento es del 2%.
    # Si el precio es mayor o igual a 100, el descuento es del 10%.
    # *Ejemplos*:
        # 120 → 108
        #  40 → 39.2

final_price = 0
discount = 0

product_price = int(input("Enter the product price:\n"))
if(product_price < 100):
    discount = product_price * 0.02
    final_price = product_price - discount
else:
    discount = product_price * 0.1
    final_price = product_price - discount
print("Product's final price is: ",final_price)



