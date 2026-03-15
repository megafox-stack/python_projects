from enemy import Enemy

class hoglin(Enemy):

    def __init__(self):
        super().__init__("Hoglin", 120, 25)

    def attack(self, enemy):
        super().attack(enemy)
        print(f"{self.name} used a smash attack!")  