# Importing the created class
import os
from character import Hero, Enemy
from weapon import iron_sword, short_bow
from consumable import HealthPotion, Bomb, PoisonBomb

def run() -> None:
    # Instanciating the class, getting two objects
    hero = Hero(name="Hero", health=100, strength=5, weapon=iron_sword, secondary_weapon=short_bow)
    enemy = Enemy(name="Enemy", health=25, strength=3, weapon=short_bow)

    # Adding 1 potion for testing
    hero.consumables[0].quantity += 1
    # Adding 1 bomb for testing
    hero.consumables[1].quantity += 1
    # Adding 1 poison bomb for testing
    hero.consumables[2].quantity += 1
    while True:
        # Draw hero and enemy bars
        hero.health_bar.draw()
        enemy.health_bar.draw()

        # Input action
        action = input("\nSelect your action: \nAttack - A\nBlock - B\nSwap Weapon - S\nItem - I\n")
        # Clear terminal
        os.system('cls')

        # Checks action
        # If attacking
        if action.upper() == "A":
            # Checks if enemy has ranged advantage
            if (hero.weapon.weapon_type == "Melee" and enemy.weapon.weapon_type == "Ranged"):
                # If yes, enemy attacks first
                enemy.attack(hero)
                hero.attack(enemy)
                # Checks if hero is poisoned and inflict damage / checks if enemy is poisoned and inflict damage
                hero.check_poisoned()
                enemy.check_poisoned()
            # Possible (hero x enemy): melee x melee, ranged x ranged, throw x melee, throw x ranged, ranged x mele
            else:
                # Hero attacks first
                hero.attack(enemy)
                enemy.attack(hero)
                # Checks if hero is poisoned and inflict damage / checks if enemy is poisoned and inflict damage
                hero.check_poisoned()
                enemy.check_poisoned()
        # If blocking
        elif action.upper() == "B":
            # Hero blocks
            hero.block()
            # Enemy attacks
            enemy.attack(hero)
            # Checks if hero is poisoned and inflict damage / checks if enemy is poisoned and inflict damage
            hero.check_poisoned()
            enemy.check_poisoned()
        # If swapping items
        elif action.upper() == "S":
            # Hero swaps item
            hero.swap(item=hero.weapon)
            # Enemy attacks
            enemy.attack(hero)
            # Checks if hero is poisoned and inflict damage / checks if enemy is poisoned and inflict damage
            hero.check_poisoned()
            enemy.check_poisoned()

        # If selecting items
        elif action.upper() == "I":
            # Show item menu
            action = input("\nSelect your item: Potion - P\nBomb - B\nPoison Bomb - PB\n")
            # Clear terminal
            os.system('cls')
            # If using potion
            if action.upper() == "P":
                # Check if health potion quantity > 0
                if hero.consumables[0].quantity > 0:
                    # Call restore method -> Hero restores health
                    HealthPotion.restore(hero.consumables[0])
                    # Reduce item quantity
                    hero.consumables[0].quantity -= 1
                    # Enemy attacks
                    enemy.attack(hero)
                    print(f"You have {hero.consumables[0].quantity} {hero.consumables[0].name} remaining")
                    # Checks if hero is poisoned and inflict damage / checks if enemy is poisoned and inflict damage
                    hero.check_poisoned()
                    enemy.check_poisoned()
                else:
                    # No item available, retry
                    print(f"No {hero.consumables[0].name} in inventory")
            # If using bomb
            elif action.capitalize() == "B":
                # Check if bomb quantity > 0
                if hero.consumables[1].quantity > 0:
                    # Call explode method -> enemy takes bomb damage
                    Bomb.explode(hero.consumables[1], enemy)
                    # Reduce item quantity
                    hero.consumables[1].quantity -= 1
                    # Enemy attacks
                    enemy.attack(hero)
                    print(f"You have {hero.consumables[1].quantity} {hero.consumables[1].name} remaining")
                    # Checks if hero is poisoned and inflict damage / checks if enemy is poisoned and inflict damage
                    hero.check_poisoned()
                    enemy.check_poisoned()
                else:
                    print(f"No {hero.consumables[1].name} in inventory")
            # If using poison bomb
            elif action.upper() == "PB":
                # Check if poison bomb quantity > 0
                if hero.consumables[2].quantity > 0:
                    # Call explode method -> enemy takes poison bomb damage
                    PoisonBomb.explode(hero.consumables[2], enemy)
                    # Call poison bomb's method poison -> enemy gets poisoned
                    PoisonBomb.poison(hero.consumables[2], enemy)
                    # Reduce item quantity
                    hero.consumables[2].quantity -= 1
                    print(f"You have {hero.consumables[2].quantity} {hero.consumables[2].name} remaining")
                    # Checks if hero is poisoned and inflict damage / checks if enemy is poisoned and inflict damage
                    hero.check_poisoned()
                    enemy.check_poisoned()
                else:
                    print(f"No {hero.consumables[2].name} in inventory")
            else:
                print("Wrong command")
        else:
            print("Wrong command")

        # Printing health bar
        hero.health_bar.draw()
        enemy.health_bar.draw()
        if enemy.health <= 0:
            print("Victory!")
            input("Press enter to start again")
            os.system('cls')
            run()
        elif hero.health <= 0:
            print("Defeat!")
            input("Press enter to start again")
            os.system('cls')
            run()
        else:
            input("Press enter to continue")

        os.system('cls')

run()
