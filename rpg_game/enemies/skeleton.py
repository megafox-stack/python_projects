from .base_enemy import Enemy

class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton", health=20, attack_power=3)