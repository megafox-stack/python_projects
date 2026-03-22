from .base_boss import Base_Boss

class ShadowBeast(Base_Boss):
    def __init__(self):
        super().__init__(name="Shadow Beast", health=150, attack_power=30)

    def special_attack(self):
        return f"{self.name} strikes with a shadowy touch!"
        player.take_damage(self.attack_power * 10)