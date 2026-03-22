class HealthPotion:
    def __init__(self, name, heal_amount):
        self.name = name
        self.heal_amount = heal_amount

    def use(self, character):
        print(f"{character.name} uses {self.name} and heals for {self.heal_amount} health!")
        character.heal(self.heal_amount)