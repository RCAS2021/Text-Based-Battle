from weapon import Weapon
from consumable import HealthPotion, Bomb, PoisonBomb
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
        # Calculate total damage
        total_damage = self.strength + self.weapon.damage
        # Check if target is hero
        if isinstance(target, Hero):
            # Check if target is blocking
            if target.is_blocking is True:
                total_damage //= 2
                target.is_blocking = False
        # Reduce health
        target.health -= total_damage
        # Prevent health going lower than 0
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {total_damage} damage to {target.name} with {self.weapon.name}")

    # Method to check if poisoned and deal damage if positive
    def check_poisoned(self) -> None:
        if self.is_poisoned is True:
            # Reduce health
            self.health -= 3
            # Prevent health going lower than 0
            self.health = max(self.health, 0)
            print(f"{self.name} took 3 damage to poison")

class Hero(Character):
    def __init__(self, name:str, health: int, strength: float, weapon: Weapon, secondary_weapon: Weapon, is_poisoned: bool = False) -> None:
        super().__init__(name=name, health=health, strength=strength, weapon=weapon, is_poisoned=is_poisoned)

        self.default_weapon = self.weapon
        self.secondary_weapon = secondary_weapon
        self.health_bar = HealthBar(self, color="green")
        self.is_blocking = False
        # Consumables[0] = Small health potion, consumables[1] = Bomb, consumables[2] = Poison bomb
        self.consumables = [HealthPotion(self, name="Small health potion", consumable_type="restoring", effect="restore 20 health", value=5, power=20, quantity=0),
                             Bomb(self, name="Bomb", consumable_type="damage", effect="deal 20 damage", value=5, power=20, quantity=0),
                             PoisonBomb(self, name="Poison bomb", consumable_type="damage", effect="deal 5 damage and poison", value=7, power=5, quantity=0)
                            ]

    # Method for blocking
    def block(self) -> None:
        self.is_blocking = True
        print(f"{self.name} blocked the attack, halving damage taken")

    # Method for equipping new item
    def equip(self, item) -> None:
        if isinstance(item, Weapon):
            self.weapon = item
        print(f"{self.name} equipped {self.weapon.name}")

    # Method for dropping item
    def drop(self, item) -> None:
        if isinstance(item, Weapon):
            self.weapon = item
        print(f"{self.name} dropped {self.weapon.name}")

    # Method for swapping items
    def swap(self, item) -> None:
        # Check if item is an instance of a weapon
        if isinstance(item, Weapon):
            # Saves old_weapon
            old_weapon = self.weapon
            # Drops current weapon
            self.drop(self.weapon)
            # Equips secondary weapon
            self.equip(self.secondary_weapon)
            # Changes secondary weapon to be old weapon
            self.secondary_weapon = old_weapon


class Enemy(Character):
    def __init__(self, name:str, health: int, strength: float, weapon: Weapon, is_poisoned: bool = False) -> None:
        super().__init__(name=name, health=health, strength=strength, weapon=weapon, is_poisoned=is_poisoned)

        self.health_bar = HealthBar(self, color="red")
