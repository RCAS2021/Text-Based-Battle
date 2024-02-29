from weapon import *
from consumable import *
from health_bar import HealthBar

class Character:
    # Variables created before the __init__ method are class-level variables, shared across all instances of the class
    def __init__(self, name: str, health: float, strength: float, weapon: Weapon, is_poisoned: bool = False) -> None:
        # Character Attributes
        self.health = health
        self.name = name
        self.max_health = health
        self.strength = strength
        self.is_poisoned = is_poisoned

        # Character inventory
        self.weapon = weapon

    # Method to calculate damage taken and health bar update
    def attack(self, target) -> None:
        total_damage = self.strength + self.weapon.damage
        if isinstance(target, Hero):
            if target.is_blocking is True:
                total_damage //= 2
                target.is_blocking = False
        target.health -= total_damage
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {total_damage} damage to {target.name} with {self.weapon.name}")


    def check_poisoned(self) -> None:
        if self.is_poisoned is True:
            self.health -= 3
            self.health = max(self.health, 0)
            print(f"{self.name} took 3 damage to poison")

class Hero(Character):
    def __init__(self, name:str, health: int, strength: float, weapon: Weapon, secondary_weapon: Weapon, is_poisoned: bool = False) -> None:
        super().__init__(name=name, health=health, strength=strength, weapon=weapon, is_poisoned=is_poisoned)

        self.default_weapon = self.weapon
        self.secondary_weapon = secondary_weapon
        self.health_bar = HealthBar(self, color="green")
        self.is_blocking = False
        # Consumables[0] = small_health_potions
        self.consumables = [HealthPotion(self, name="small_health_potion", consumable_type="restoring", effect="restore 20 health", value=5, power=20, quantity=0),
                             Bomb(self, name="Bomb", consumable_type="damage", effect="deal 20 damage", value=5, power=20, quantity=0),
                             PoisonBomb(self, name="PoisonBomb", consumable_type="damage", effect="deal 5 damage and poison", value=7, power=5, quantity=0)
                            ]

    def block(self):
        print(f"{self.name} blocked the attack, halving damage taken")
        self.is_blocking = True

    def equip(self, item) -> None:
        if isinstance(item, Weapon):
            self.weapon = item
        print(f"{self.name} equipped {self.weapon.name}")

    def drop(self, item) -> None:
        if isinstance(item, Weapon):
            self.weapon = item
        print(f"{self.name} dropped {self.weapon.name}")

    def swap(self, item) -> None:
        if isinstance(item, Weapon):
            old_weapon = self.weapon
            self.drop(self.weapon)
            self.equip(self.secondary_weapon)
            self.secondary_weapon = old_weapon


class Enemy(Character):
    def __init__(self, name:str, health: int, strength: float, weapon: Weapon, is_poisoned: bool = False) -> None:
        super().__init__(name=name, health=health, strength=strength, weapon=weapon, is_poisoned=is_poisoned)

        self.health_bar = HealthBar(self, color="red")
