from enemy import Enemy

class orc(Enemy):

    def __init__(self):
        super().__init__("Orc", 100, 20)

    def attack(self, enemy):
        super().attack(enemy)
        print(f"{self.name} used a powerful attack!")  