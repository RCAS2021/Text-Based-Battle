# Importing the created class
from character import Character

# Instanciating the class, getting two objects
hero = Character(name="Hero", health=100, damage=5)
enemy = Character(name="enemy", health=25, damage=3)

while True:
    # Calling attack methods
    hero.attack(enemy)
    enemy.attack(hero)

    # Printing current health
    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    # Waiting input to continue
    input("Continue...")
