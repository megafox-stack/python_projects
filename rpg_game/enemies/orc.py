from .base_enemy import Enemy

class Orc(Enemy):
    def __init__(self):
        super().__init__(name="Orc", health=50, attack_power=10)