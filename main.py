# Importing the created class
import os
from character import Hero, Enemy
from weapon import *

# Instanciating the class, getting two objects
hero = Hero(name="Hero", health=100, strength=5, weapon=iron_sword, secondary_weapon=short_bow)
enemy = Enemy(name="enemy", health=25, strength=3, weapon=fists)

while True:
    os.system("cls")
    # Printing health bar
    hero.health_bar.draw()
    enemy.health_bar.draw()
    # Calling attack methods
    hero.attack(enemy)
    enemy.attack(hero)

    swapping = input("\nSwap weapons? Y/N\n")
    if swapping.upper() == "Y":
        hero.swap(item=hero.weapon)
