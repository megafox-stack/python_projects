from enemies.base_enemy import Enemy

class Base_Boss(Enemy):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

    def special_attack(self):
        return f"{self.name} uses a special attack!"
        player.take_damage(self.attack_power * 4)     