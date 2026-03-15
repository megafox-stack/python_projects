class charecter:
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self,enemy):
        enemy.health -= self.attack_power
        print(f"{self.name} attacked {enemy.name} for {self.attack_power} damage!")    

        def is_alive(self):
            return self.health > 0
        
