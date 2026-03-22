from .base_enemy import Enemy

class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", health=30, attack_power=5)