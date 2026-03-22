
from rpg_game.characters.hero import Hero

from bosses.orc_warlord import OrcWarlord
from bosses.shadow_beast import ShadowBeast

from portions.healthportion import HealthPotion

from weapons.sword import Sword
from weapons.bow import Bow

from enemies.dragon import Dragon
from enemies.goblin import Goblin
from enemies.hoglin import Hoglin
from enemies.skeleton import Skeleton
from enemies.orc import Orc

def battle(player, enemy):

    while player.is_alive() and enemy.is_alive():
        print("\n1. Attack")
        print("2. Heal")

        choice = input("Choose an action: ")

        if choice == "1":
            player.attack(enemy)

        elif choice == "2":
            potion = HealthPotion()
            potion.use(player)

        if enemy.is_alive():
            enemy.attack(player)

        player.show_status()
        enemy.show_status()

   
    if player.is_alive():
        print(f"\n🔥 {player.name} wins!")
    else:
        print("\n💀 Game Over!")


hero = Hero(name = "rob")
hero.equip_weapon(Sword())

enemy = Goblin()
battle(hero,enemy)

print("BOSS FIGHT!!!!!")
boss = ShadowBeast()
battle(hero,boss)