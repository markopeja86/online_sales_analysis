# main.py
from product import Product
from product_manager import ProductManager
from cart import Cart

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
    
    cart = Cart()
    cart.add_to_cart(product1)
    cart.add_to_cart(product2)

    print("Products in cart:")
    for item in cart.display_cart():
        print(item)

    print(f"Total cart value: {cart.total_cart_value()}")
if __name__ == "__main__":
    main()
