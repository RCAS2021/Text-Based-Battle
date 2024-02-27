# Hotfix for printing correct colors
import os

os.system("")

class HealthBar():
    # Symbol for remaining health
    symbol_remaining: str = chr(9608)
    # Symbol for lost health
    symbol_lost: str = "_"
    # Barrier
    barrier: str = "|"
    # Possible colors
    colors: dict = {"red": "\033[91m",
                    "purple": "\033[95m",
                    "blue": "\033[34m",
                    "blue2": "\033[36m",
                    "blue3": "\033[96m",
                    "green": "\033[92m",
                    "grey": "\033[37m",
                    "default": "\033[0m"
                    }

    # Constructor method
    def __init__(self, entity, length:int = 20, is_colored: bool = True, color: str = "") -> None:
        # Entity values
        self.entity = entity
        self.current_value = entity.health
        self.max_value = entity.max_health

        # Health Bar values
        self.length = length
        self.is_colored = is_colored
        self.color = self.colors.get(color, self.colors.get("default"))

    # Updates current value to the entity's health
    def update(self) -> None:
        self.current_value = self.entity.health

    # Draws the health bar
    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s HEALTH: {self.entity.health}/{self.entity.max_health}")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}"
              )
