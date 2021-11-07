from project.decoration.plant import Plant
from project.decoration.ornament import Ornament
from project.fish.saltwater_fish import SaltwaterFish
from project.fish.freshwater_fish import FreshwaterFish
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.decoration.decoration_repository import DecorationRepository


class Controller:
    __VALID_AQUARIUM_TYPES = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium,
    }
    __VALID_DECORATION_TYPES = {
        "Ornament": Ornament,
        "Plant": Plant,
    }
    __VALID_FISH_TYPES = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish,
    }

    def __init__(self) -> None:
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.__VALID_AQUARIUM_TYPES:
            return f"Invalid aquarium type."

        aquarium = self.__VALID_AQUARIUM_TYPES[aquarium_type](aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str) -> str:
        if decoration_type not in self.__VALID_DECORATION_TYPES:
            return f"Invalid decoration type."

        decoration = self.__VALID_DECORATION_TYPES[decoration_type]()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str) -> str:
        aquarium = self.find_aquarium_by_name(aquarium_name)
        if aquarium is not None:
            decoration = self.decorations_repository.find_by_type(decoration_type)
            if decoration == "None":
                return f"There isn't a decoration of type {decoration_type}."

            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float) -> str:
        if fish_type not in self.__VALID_FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."

        fish = self.__VALID_FISH_TYPES[fish_type](fish_name, fish_species, price)
        aquarium = self.find_aquarium_by_name(aquarium_name)
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        fed_fish_count = aquarium.feed()
        return f"Fish fed: {fed_fish_count}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        fish_value = sum([f.price for f in aquarium.fish])
        decorations_value = sum([d.price for d in aquarium.decorations])
        return f"The value of Aquarium {aquarium_name} is {fish_value + decorations_value:.2f}."

    def report(self):
        info = [str(aquarium) for aquarium in self.aquariums]
        return '\n'.join(info)

    def find_aquarium_by_name(self, aquarium_name: str):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
