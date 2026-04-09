class CalculatorHistory:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        res = a + b
        self.history.append(f"{a} + {b} = {res}")
        return res
    
    def view_history(self):
        for item in self.history:
            print(item)

    def clear_history(self):
        self.history.clear()

    def last_result(self):
        if len(self.history) == 0:
            return f"Empty"
        else:
            return self.history[-1]
        

ch = CalculatorHistory()
ch.add(10, 10)
ch.add(10, 15)
ch.add(10, 20)
ch.view_history()
print(f"Last Result: {ch.last_result()}")

