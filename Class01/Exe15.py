import math

class Vetor2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vetor2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

v1 = Vetor2D(3, 4)
v2 = Vetor2D(1, 2)
print(v1)
print(v1 + v2)
print(v1 == v2)
print(v1.magnitude())