class Consumable:
    def __init__(self, entity, name: str, consumable_type: str, effect: str, value: int) -> None:
        self.entity = entity
        self.name = name
        self.consumable_type = consumable_type
        self.effect = effect
        self.value = value

class HealthPotion(Consumable):
    def __init__(self, entity, name: str, consumable_type: str, effect: str, value: int = 5, power:int = 20) -> None:
        super().__init__(entity = entity, name=name, consumable_type=consumable_type, effect=effect, value=value)

        self.power = power

    def restore(self) -> None:
        if self.entity.health + self.power > self.entity.max_health:
            self.entity.health = self.entity.max_health
        else:
            self.entity.health += self.power
        print(f"{self.entity.name} healed for {self.power}")
        self.entity.health_bar.update()
