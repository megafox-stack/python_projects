from characters.character import Character

class Enemy(Character):

    enemy_count = 0

    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        Enemy.enemy_count += 1