from charectars.base_charectar import base_charectar

class hero(base_charectar):
    def __init__(self, name):
        super().__init__(name, health=1000, attack_power=15)

