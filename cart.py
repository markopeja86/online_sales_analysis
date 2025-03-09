# cart.py
class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def total_cart_value(self):
        return sum(item.price * item.quantity for item in self.cart_items)

    def display_cart(self):
        return [f"{item.name}: {item.quantity} x {item.price}" for item in self.cart_items]
