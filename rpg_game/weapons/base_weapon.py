class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.damage} damage!")
        target.take_damage(self.damage)