# Importing the created class
import os
from character import Hero, Enemy
from weapon import *

# Instanciating the class, getting two objects
hero = Hero(name="Hero", health=100, strength=5, weapon=iron_sword, secondary_weapon=short_bow)
enemy = Enemy(name="enemy", health=25, strength=3, weapon=fists)

while True:
    hero.health_bar.draw()
    enemy.health_bar.draw()
    # Input action
    action = input("\nSelect your action: \nAttack - A\nBlock - B\nSwap Weapon- S\n")
    os.system("cls")
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
    input("Press any button to continue")
    os.system("cls")
