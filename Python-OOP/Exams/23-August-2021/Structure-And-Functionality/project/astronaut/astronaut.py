from abc import ABC, abstractmethod


class Astronaut(ABC):
    OXYGEN_DECREASING_PER_BREATHE = 10

    def __init__(self, name: str, oxygen: int) -> None:
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self) -> property:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        if not value or value == ' ':
            raise ValueError(f"Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    @abstractmethod
    def breathe(self) -> None:
        pass

    def increase_oxygen(self, amount: int) -> None:
        self.oxygen += amount

    def __str__(self) -> str:
        backpack = f"none" if not self.backpack else ", ".join(self.backpack)
        return f"Name: {self.name}\n" \
               f"Oxygen: {self.oxygen}\n" \
               f"Backpack items: {backpack}"
