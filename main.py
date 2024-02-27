# Importing the created class
from character import Character
from weapon import *

# Instanciating the class, getting two objects
hero = Character(name="Hero", health=100, strength=5, weapon=fists)
enemy = Character(name="enemy", health=25, strength=3, weapon=fists)

while True:
    # Calling attack methods
    hero.attack(enemy)
    enemy.attack(hero)

    # Printing current health
    print(f"{hero.name} Health: {hero.health}")
    print(f"{enemy.name} Health: {enemy.health}")
    # Waiting input to continue
    input("\nContinue...")
