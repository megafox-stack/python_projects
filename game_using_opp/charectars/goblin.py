from charectars.enemy import enemy

class goblin(enemy):

    def __init__(self):
        super().__init__("Goblin", 50, 10)

    def attack(self, enemy):
        super().attack(enemy)
        print(f"{self.name} used a sneaky attack!")    