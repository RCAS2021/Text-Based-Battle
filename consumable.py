class Consumable:
    def __init__(self, entity, name: str, consumable_type: str, effect: str, value: int, quantity: int) -> None:
        # Consumable attributes
        self.entity = entity
        self.name = name
        self.consumable_type = consumable_type
        self.effect = effect
        self.value = value
        self.quantity = quantity

class HealthPotion(Consumable):
    def __init__(self, entity, name: str, consumable_type: str, effect: str, value: int = 5, power:int = 20, quantity: int = 0) -> None:
        super().__init__(entity=entity, name=name, consumable_type=consumable_type, effect=effect, value=value, quantity=quantity)

        # Setting power
        self.power = power

    # Restore method to heal character
    def restore(self) -> None:
        # Check if after healing, health would be greater than max health (another way of checking, different from attack)
        if self.entity.health + self.power > self.entity.max_health:
            # Set health to max health
            self.entity.health = self.entity.max_health
        else:
            # Heals health by potion power
            self.entity.health += self.power
        print(f"{self.entity.name} used {self.name} to heal {self.power} health")
        # Updates health bar
        self.entity.health_bar.update()

class Bomb(Consumable):
    def __init__(self, entity, name: str, consumable_type: str, effect: str, value: int = 5, power:int = 20, quantity: int = 0) -> None:
        super().__init__(entity=entity, name=name, consumable_type=consumable_type, effect=effect, value=value, quantity=quantity)

        # Setting power
        self.power = power

    # Method for bomb explosion
    def explode(self, target) -> None:
        # Target gets damaged by bomb power
        target.health -= self.power
        # Target health goes to 0 if after taking damage it goes lower than 0
        target.health = max(target.health, 0)
        # Updates health bar
        target.health_bar.update()
        print(f"{self.entity.name} dealt {self.power} damage to {target.name} with {self.name}")

class PoisonBomb(Bomb):
    def __init__(self, entity, name: str, consumable_type: str, effect: str, value: int = 5, power:int = 20, quantity: int = 0) -> None:
        super().__init__(entity=entity, name=name, consumable_type=consumable_type, effect=effect, value=value, quantity=quantity)

        # Setting power
        self.power = power

    # Method for poisoning target
    def poison(self, target):
        # Sets target is_poisoned attribute to true
        target.is_poisoned = True
        print(f"{target.name} is now poisoned")
