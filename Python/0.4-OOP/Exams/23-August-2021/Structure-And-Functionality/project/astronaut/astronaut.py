from abc import ABC, abstractmethod


class Astronaut(ABC):
    OXYGEN_DECREASING_PER_BREATHE = 10
    
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value == ' ':
            raise ValueError(f"Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    @abstractmethod
    def breathe(self):
        pass

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __repr__(self):
        backpack = f'none' if not self.backpack else ", ".join(self.backpack)
        info = [
            f"Name: {self.name}",
            f"Oxygen: {self.oxygen}",
            f'Backpack items: {backpack}'
        ]

        return '\n'.join(info)
