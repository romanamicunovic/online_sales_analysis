from product import Product
from product_manager import ProductManager

pm = ProductManager()
pm.add_product(Product("Laptop", 1750, 3))
pm.add_product(Product("Telefon", 550, 7))
pm.add_product(Product("Slusalice", 35, 15))

pm.display_products()
print("Ukupna vrijednost inventara:", pm.total_value())