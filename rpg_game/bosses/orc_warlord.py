from .base_boss import Base_Boss

class OrcWarlord(Base_Boss):
    def __init__(self):
        super().__init__(name="Orc Warlord", health=200, attack_power=40)

    def special_attack(self):
        return f"{self.name} leads a charge!"
        player.take_damage(self.attack_power * 3)