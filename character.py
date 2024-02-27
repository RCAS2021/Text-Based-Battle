from weapon import Weapon

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
        target.health -= self.strength + self.weapon.damage
        target.health = max(target.health, 0)

class Hero(Character):
    def __init__(self, name:str, health: int, strength: float, weapon: Weapon) -> None:
        super().__init__(name=name, health=health, strength=strength, weapon=weapon)

class Enemy(Character):
    def __init__(self, name:str, health: int, strength: float, weapon: Weapon) -> None:
        super().__init__(name=name, health=health, strength=strength, weapon=weapon)
        