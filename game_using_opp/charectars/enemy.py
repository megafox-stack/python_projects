from charectars.charectar import Charectar 

class enemy(Charectar):

    enemy_count = 0

    def __init__(self,name,health,attack):
        super().init__(name,health,attack)
        enemy.enemy_count += 1