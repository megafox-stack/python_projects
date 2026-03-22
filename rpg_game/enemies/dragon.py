from .base_enemy import Enemy

class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon", health=100, attack_power=40)