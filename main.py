from product import Product
from product_manager import ProductManager
from cart import Cart

pm = ProductManager()
pm.add_product(Product("Laptop", 1750, 3))
pm.add_product(Product("Telefon", 550, 7))
pm.add_product(Product("Slusalice", 35, 15))

pm.display_products()
print("Ukupna vrijednost inventara:", pm.total_value())

cart = Cart()
cart.add_to_cart(pm.products[0])
cart.add_to_cart(pm.products[1])
cart.add_to_cart(pm.products[2])

cart.display_cart()
print("Ukupna vrijednost korpe:", cart.total_cart_values())