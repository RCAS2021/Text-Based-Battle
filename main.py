# Importing the created class
from character import Hero, Enemy
from weapon import *

# Instanciating the class, getting two objects
hero = Hero(name="Hero", health=100, strength=5, weapon=iron_sword)
enemy = Enemy(name="enemy", health=25, strength=3, weapon=fists)

while True:
    print(f"{hero.name} Health: {hero.health}")
    print(f"{enemy.name} Health: {enemy.health}")
    # Calling attack methods
    hero.attack(enemy)
    enemy.attack(hero)

    # Printing current health
    print(f"{hero.name} Health: {hero.health}")
    print(f"{enemy.name} Health: {enemy.health}")
    # Waiting input to continue
    input("\nContinue...")
