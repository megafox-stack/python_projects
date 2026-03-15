from charectars.enemy import enemy

class dragon(enemy):
    def __init__(self):
        super().__init__("Dragon", 200, 25)

    def attack(self, enemy):
        super().attack(enemy)
        print(f"{self.name} used a fiery breath attack!")