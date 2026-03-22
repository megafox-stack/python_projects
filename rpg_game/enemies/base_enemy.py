class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        return self.attack_power

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0
    
    def attack_player(self, player):
        damage = self.attack()
        player.take_damage(damage)
        print(f"{self.name} attacks you for {damage} damage!")