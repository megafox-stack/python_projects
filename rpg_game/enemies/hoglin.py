from .base_enemy import Enemy

class Hoglin(Enemy):
    def __init__(self):
        super().__init__(name="Hoglin", health=120, attack_power=30)