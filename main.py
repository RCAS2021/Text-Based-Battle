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
    hero.consumables[1].quantity += 1
    while True:
        hero.health_bar.draw()
        enemy.health_bar.draw()
        # Input action
        action = input("\nSelect your action: \nAttack - A\nBlock - B\nSwap Weapon - S\nItem - I\n")
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
        elif action.upper() == "S":
            hero.swap(item=hero.weapon)
            enemy.attack(hero)
        elif action.upper() == "I":
            action = input("\nSelect your item: Potion - P\nBomb - B\n")
            os.system('cls')
            if action.upper() == "P":
                # Check if health potion quantity > 0
                if hero.consumables[0].quantity > 0:
                    HealthPotion.restore(hero.consumables[0])
                    hero.consumables[0].quantity -= 1
                    enemy.attack(hero)
                    print(f"You have {hero.consumables[0].quantity} {hero.consumables[0].name} remaining")
                else:
                    print(f"No {hero.consumables[0].name} in inventory")
            elif action.capitalize() == "B":
                if hero.consumables[1].quantity > 0:
                    Bomb.explode(hero.consumables[1], enemy)
                    hero.consumables[1].quantity -= 1
                    print(f"You have {hero.consumables[1].quantity} {hero.consumables[1].name} remaining")
                else:
                    print(f"No {hero.consumables[1].name} in inventory")
            else:
                print("Wrong command")
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
