class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person3 = Person("Charlie", 22)

person1.introduce()
person2.introduce()
person3.introduce()