class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name} for {self.attack_power} damage!")
        enemy.take_damage(self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Remaining health: {self.health}")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount} health! Current health: {self.health}")
    def is_alive(self):
        return self.health > 0
    def show_stats(self):
        print(f"{self.name} - Health: {self.health}, Attack Power: {self.attack_power}")
            