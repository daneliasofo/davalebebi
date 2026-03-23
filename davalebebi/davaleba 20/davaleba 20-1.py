class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def sell(self, qty):
        if qty <= self.amount:
            self.amount -= qty
            print(f"Sold {qty}. Remaining: {self.amount}")
        else:
            print("Not enough product")


p = Product("Laptop", 1200, 10)

p.sell(3)
p.sell(5)
p.sell(5) 