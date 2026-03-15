from characters.enemy import Enemy

class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon", 200, 25)

    def attack(self, enemy):
        super().attack(enemy)
        print(f"{self.name} used a fiery breath attack!")