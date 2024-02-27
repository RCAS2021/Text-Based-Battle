# Importing the created class
from character import Hero, Enemy
from weapon import *

# Instanciating the class, getting two objects
hero = Hero(name="Hero", health=100, strength=5, weapon=iron_sword)
enemy = Enemy(name="enemy", health=25, strength=3, weapon=fists)

def print_health(character):
    print(f"{character.name} Health: {character.health}")

# Printing current health at battle start
print_health(hero)
print_health(enemy)
print()

while True:
    # Calling attack methods
    hero.attack(enemy)
    enemy.attack(hero)
    print()
    print("--- End Turn ---")

    # Printing current health
    print_health(hero)
    print_health(enemy)

    # Waiting input to continue
    input("\nContinue...")
