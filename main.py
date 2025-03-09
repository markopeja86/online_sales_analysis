# main.py
from product import Product
from product_manager import ProductManager

def main():
    # Kreiranje ProductManager instance
    manager = ProductManager()

    # Dodavanje proizvoda
    product1 = Product("Laptop", 1000, 5)
    product2 = Product("Phone", 500, 10)
    product3 = Product("Headphones", 150, 20)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    # Prikazivanje proizvoda
    print("Products in inventory:")
    for info in manager.display_products():
        print(info)

    # Prikazivanje ukupne vrednosti inventara
    print(f"Total inventory value: {manager.total_inventory_value()}")

if __name__ == "__main__":
    main()
