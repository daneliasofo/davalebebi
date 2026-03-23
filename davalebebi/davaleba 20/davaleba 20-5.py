class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total


cart = Cart()

cart.add_item(Item("Phone", 800))
cart.add_item(Item("Headphones", 150))
cart.add_item(Item("Mouse", 50))

print("Total price:", cart.total_price())