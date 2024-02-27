# Importing the created class
import os
from character import Hero, Enemy
from weapon import *

def run() -> None:
    # Instanciating the class, getting two objects
    hero = Hero(name="Hero", health=100, strength=5, weapon=iron_sword, secondary_weapon=short_bow)
    enemy = Enemy(name="Enemy", health=25, strength=3, weapon=fists)

    while True:
        hero.health_bar.draw()
        enemy.health_bar.draw()
        # Input action
        action = input("\nSelect your action: \nAttack - A\nBlock - B\nSwap Weapon- S\n")
        os.system('cls')
        if action.upper() == "A":
            hero.attack(enemy)
        elif action.upper() == "B":
            hero.block()
        elif action.upper() == "S":
            hero.swap(item=hero.weapon)
        else:
            print("Wrong command")

        enemy.attack(hero)
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
