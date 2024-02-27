from weapon import *

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
        target.health -= total_damage
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {total_damage} damage to {target.name} with {self.weapon.name}")

class Hero(Character):
    def __init__(self, name:str, health: int, strength: float, weapon: Weapon) -> None:
        super().__init__(name=name, health=health, strength=strength, weapon=weapon)

        self.default_weapon = self.weapon

    def equip(self, item) -> None:
        if type(item) == Weapon:
            self.weapon = item
        print(f"{self.name} equipped {self.weapon.name}")

    def drop(self, item) -> None:
        if type(item) == Weapon:
            self.weapon = self.default_weapon
        print(f"{self.name} dropped {self.weapon.name}")


class Enemy(Character):
    def __init__(self, name:str, health: int, strength: float, weapon: Weapon) -> None:
        super().__init__(name=name, health=health, strength=strength, weapon=weapon)
        