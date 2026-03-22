from .base_boss import Base_Boss

class FireMegaDragon(Base_Boss):
    def __init__(self):
        super().__init__(name="Fire Mega Dragon", health=300, attack_power=50)

    def special_attack(self):
        return f"{self.name} unleashes a fiery breath!"
        player.take_damage(self.attack_power * 2)