from charectar import charecter

class player(charecter):
        def __init__(self,name,portions):
            super().__init__(name,100,15)
            self.portions = portions
        def use_portion(self):
            if self.portions > 0:
                self.health += 20
                self.portions -= 1
                print(f"{self.name} used a portion and restored health! Current health: {self.health}")
            else:
                print("No portions left!")
                