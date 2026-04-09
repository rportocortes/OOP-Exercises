class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        f = (self.celsius * 1.8) + 32
        return f

    def to_kelvin(self):
        k = self.celsius + 273.15
        return k
        
    def __str__(self):
        return f"Celsius: {self.celsius} | Fahrenheit: {self.to_fahrenheit()} | Kelvin: {self.to_kelvin()}"
    
t1 = Temperature(45)
print(t1)
        