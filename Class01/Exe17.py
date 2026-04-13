class Matrix:
    def __init__(self, rows, cols):
        self.grid = [[0] * cols for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def set(self, r, c, v):
        self.grid[r][c] = v

    def get(self, r, c):
        return self.grid[r][c]

    def __str__(self):
        result = ""
        for row in self.grid:
            result += " ".join(str(v) for v in row) + "\n"
        return result

    def add(self, other):
        result = Matrix(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                result.set(r, c, self.grid[r][c] + other.grid[r][c])
        return result

m1 = Matrix(2, 2)
m1.set(0, 0, 1)
m1.set(1, 1, 3)

m2 = Matrix(2, 2)
m2.set(0, 0, 2)
m2.set(1, 1, 4)

print(m1)
print(m1.add(m2))