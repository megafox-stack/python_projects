from base_weapon import Weapon

class Sword(Weapon):
    def __init__(self):
        super().__init__(name = "Sword",damage = 100)