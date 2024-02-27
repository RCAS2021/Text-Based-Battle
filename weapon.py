class Weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

fists = Weapon(name="fists", weapon_type="Melee", damage=3, value=1)

iron_sword = Weapon(name="Iron Sword", weapon_type="Melee", damage=10, value=10)

short_bow = Weapon(name="Short Bow", weapon_type="Ranged", damage=8, value=15)

throwing_knife = Weapon(name="Throwing Kinfe", weapon_type="Throwable", damage=2, value=3)
