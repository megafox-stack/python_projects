from .character import Character
class Hero(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)

