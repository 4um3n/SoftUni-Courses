from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def taken_capacity(self):
        return len(self.fish)

    @property
    def decorations_price(self):
        return sum([d.price for d in self.decorations])

    @property
    def fish_price(self):
        return sum([f.price for f in self.fish])

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError(f"Aquarium name cannot be an empty string.")
        self.__name = value

    @abstractmethod
    def add_fish(self, fish) -> str:
        pass

    def calculate_value(self) -> float:
        return self.decorations_price + self.fish_price

    def calculate_comfort(self) -> int:
        return sum([d.comfort for d in self.decorations])

    def remove_fish(self, fish) -> None:
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration) -> None:
        self.decorations.append(decoration)

    def feed(self) -> int:
        [fish.eat() for fish in self.fish]
        return self.taken_capacity

    def _can_add_fish(self) -> bool:
        return self.capacity > self.taken_capacity

    def __str__(self):
        fish = ' '.join([f.name for f in self.fish]) if self.fish else f"none"
        return f"{self.name}:\n" \
               f"Fish: {fish}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}"
