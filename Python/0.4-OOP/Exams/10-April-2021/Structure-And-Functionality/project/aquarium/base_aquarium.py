from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError(f"Aquarium name cannot be an empty string.")

        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return f"Not enough capacity."

        if type(fish).AQUARIUM == type(self).__name__:
            self.fish.append(fish)
            return f"Successfully added {type(fish).__name__} to {self.name}."

        return f"Water not suitable."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        fed_fish_count = 0
        for fish in self.fish:
            fed_fish_count += 1
            fish.eat()

        return fed_fish_count

    def __str__(self):
        info = [f"{self.name}:", f"Decorations: {len(self.decorations)}", f"Comfort: {self.calculate_comfort()}"]
        fish = "none" if not self.fish else ' '.join([f.name for f in self.fish])
        info.insert(1, f"Fish: {fish}")
        return '\n'.join(info)


