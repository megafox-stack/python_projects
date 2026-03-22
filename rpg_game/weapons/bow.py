from base_weapon import Weapon

class Bow(Weapon):
    def __init__(self):
        super().__init__(name = "Bow",damage = 40)
        
