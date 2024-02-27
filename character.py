class Character:
    # Variables created before the __init__ method are class-level variables, shared across all instances of the class
    def __init__(self, name: str, health: float, damage: float) -> None:
        self.health = health
        self.name = name
        self.max_health = health
        self.damage = damage

    def attack(self, target) -> None:
        target.health -= self.damage
        target.health = max(target.health, 0)
