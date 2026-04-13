class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        self.statement = []

    def deposit(self, amount):
        self.balance += amount
        self.statement.append(("Deposit", amount))
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.statement.append(("Withdraw", amount))
            print(f"Withdrawn: ${amount}")
        else:
            print("Insufficient funds!")

    def display(self):
        print(f"Account Owner: {self.owner}")
        print(f"Current Balance: ${self.balance:.2f}")

    def view_statement(self):
        for type, value in self.statement:
            print(f"{type}: ${value}")

    def transfer(self, other_account, amount):
        if amount <= self.balance:
            self.withdraw(amount)
            other_account.deposit(amount)
            print(f"Transferred ${amount} to {other_account.owner}")
        else:
            print("Insufficient funds!")


account1 = BankAccount("John Doe", 1000.0)
account2 = BankAccount("Ana Silva", 500.0)

account1.deposit(500)
account1.withdraw(200)
account1.transfer(account2, 300)

account1.display()
account1.view_statement()