from weapon import *
from health_bar import HealthBar

class Character:
    # Variables created before the __init__ method are class-level variables, shared across all instances of the class
    def __init__(self, name: str, health: float, strength: float, weapon: Weapon) -> None:
        # Character Attributes
        self.health = health
        self.name = name
        self.max_health = health
        self.strength = strength

        # Character inventory
        self.weapon = weapon

    def attack(self, target) -> None:

        total_damage = self.strength + self.weapon.damage
        if isinstance(target, Hero):
            if target.is_blocking is True:
                total_damage //= 2
                target.is_blocking = False
        target.health -= total_damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {total_damage} damage to {target.name} with {self.weapon.name}")

class Hero(Character):
    def __init__(self, name:str, health: int, strength: float, weapon: Weapon, secondary_weapon: Weapon) -> None:
        super().__init__(name=name, health=health, strength=strength, weapon=weapon)

        self.default_weapon = self.weapon
        self.secondary_weapon = secondary_weapon
        self.health_bar = HealthBar(self, color="green")
        self.is_blocking = False

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
    def __init__(self, name:str, health: int, strength: float, weapon: Weapon) -> None:
        super().__init__(name=name, health=health, strength=strength, weapon=weapon)

        self.health_bar = HealthBar(self, color="red")
