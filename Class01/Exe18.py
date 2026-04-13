class Character:
    def __init__(self, name, attack, defense):
        self.name = name
        self.health = 100
        self.attack = attack
        self.defense = defense

    def attack_character(self, other):
        damage = max(0, self.attack - other.defense)
        other.health -= damage
        print(f"{self.name} attacked {other.name} for {damage} damage! {other.name} has {other.health} HP left.")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} | HP: {self.health} | Attack: {self.attack} | Defense: {self.defense}"


c1 = Character("Warrior", attack=30, defense=10)
c2 = Character("Mage", attack=40, defense=5)

print(c1)
print(c2)
print()

while c1.is_alive() and c2.is_alive():
    c1.attack_character(c2)
    if c2.is_alive():
        c2.attack_character(c1)

if c1.is_alive():
    print(f"\n{c1.name} wins!")
else:
    print(f"\n{c2.name} wins!")