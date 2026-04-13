import random

class GuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10

    def guess(self, n):
        self.attempts += 1
        if n == self.number:
            print(f"Correct! You got it in {self.attempts} attempts.")
        elif n < self.number:
            print("Too low!")
        else:
            print("Too high!")
        if self.attempts >= self.max_attempts and n != self.number:
            print(f"Game over! The number was {self.number}.")

    def restart(self):
        self.number = random.randint(1, 100)
        self.attempts = 0
        print("Game restarted!")

game = GuessingGame()
game.guess(50)
game.guess(75)
game.guess(90)