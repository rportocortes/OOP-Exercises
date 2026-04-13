class Stack:
    def __init__(self):
        self.item = []

    def push(self, value):
        self.item.append(value)
        
    def pop(self):
        if not self.item:
            return None
        return self.item.pop()
    
    def peek(self):
        if not self.item:
            return None
        return self.item[-1]
    
    def is_empty(self):
        return len(self.item) == 0
        
s1 = Stack()
s1.push("Book")
s1.push("Bag")
s1.push("Dish")
print(s1.pop())
print(s1.peek())
print(s1.is_empty())
