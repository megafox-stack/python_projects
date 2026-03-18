from charectars.hero import Hero
from bosses.fire_mega_dragon import fire_mega_dragon
from bosses.shadow_beast import shadow_beast
from bosses.orc_warlord import orc_warlord
from portions.healthportion import healthportion
from weapons.sword import sword
from weapons.bow import bow
from enemies.dragon import dragon
from enemies.goblin import goblin
from enemies.hoglin import hoglin
from enemies.skeleton import skeleton   
from enemies.orc import orc

def battle(player,enemy):
    while player.isalive() and enemy.isalive():
        print("1. Attack")
        print("2. Heal")

        choice = input("Choose an action: ")

        if choice == "1":
            player.attack(enemy)
        elif choice == "2":
            portion = healthportion()
            portion.use(player)        
        
        if enemy.isalive():
            enemy.attack(player)
            
        if player.isalive():
            print(f"{player.name} wins!")
        else:
            print("Game Over!")


hero = Hero(name = "rob")
hero.equip_weapon(sword())

enemy = goblin()
battle(hero,enemy)

print("BOSS FIGHT!!!!!")
boss = shadow_beast()
battle(hero,boss)