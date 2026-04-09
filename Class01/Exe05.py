class Product:
    def __init__(self, name, price, inventory):
        self.name = name
        self.price = price
        self.inventory = inventory

    def sell(self, qty):
        if qty > self.inventory or qty <= 0:
            return False
        self.inventory -= qty
        return self.inventory

    def restock(self, qty):
        if qty <= 0:
            return False
        self.inventory += qty
        return self.inventory

    
p1 = Product("Water", 3.00, 45)
print(p1.sell(3))
print(p1.restock(1))