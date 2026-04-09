class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(f"Brand: {self.brand} | Model: {self.model} | Year: {self.year}")

car1 = Car("Toyota", "Corolla", 2024)
car2 = Car("Ford", "Mustang", 1969)

car1.display()
car2.display()