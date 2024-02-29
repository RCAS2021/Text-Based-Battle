# Importing the created class
import os
from character import Hero, Enemy
from weapon import *
from consumable import *

def run() -> None:
    # Instanciating the class, getting two objects
    hero = Hero(name="Hero", health=100, strength=5, weapon=iron_sword, secondary_weapon=short_bow)
    enemy = Enemy(name="Enemy", health=25, strength=3, weapon=short_bow)

    # Adding 1 potion for testing
    hero.consumables[0].quantity += 1
    while True:
        hero.health_bar.draw()
        enemy.health_bar.draw()
        # Input action
        action = input("\nSelect your action: \nAttack - A\nBlock - B\nSwap Weapon - S\nHeal - H\n")
        os.system('cls')
        if action.upper() == "A":
            if (hero.weapon.weapon_type == "Melee" and enemy.weapon.weapon_type == "Ranged"):
                enemy.attack(hero)
                hero.attack(enemy)
            # Possible (hero x enemy): melee x melee, ranged x ranged, throw x melee, throw x ranged, ranged x mele
            else:
                hero.attack(enemy)
                enemy.attack(hero)

        elif action.upper() == "B":
            hero.block()
            enemy.attack(hero)
        elif action.upper() == "H":
            enemy.attack(hero)
            hero.small_heal()
            print(f"You have {hero.consumables[0].quantity} {hero.consumables[0].name}")
        elif action.upper() == "S":
            hero.swap(item=hero.weapon)
            enemy.attack(hero)
        else:
            print("Wrong command")

        # Printing health bar
        hero.health_bar.draw()
        enemy.health_bar.draw()
        if enemy.health <= 0:
            print("Victory!")
            input("Press any button to start again")
            os.system('cls')
            run()
        elif hero.health <= 0:
            print("Defeat!")
            input("Press any button to start again")
            os.system('cls')
            run()
        else:
            input("Press any button to continue")

        os.system('cls')

run()
