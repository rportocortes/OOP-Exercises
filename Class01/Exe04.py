class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Insufficient funds!")

    def display(self):
        print(f"Account Owner: {self.owner}")
        print(f"Current Balance: ${self.balance:.2f}")


account = BankAccount("John Doe", 1000.0)
account.deposit(500)
account.withdraw(200)
account.display()