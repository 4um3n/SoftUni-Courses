from project.decoration.plant import Plant
from project.decoration.ornament import Ornament
from project.fish.saltwater_fish import SaltwaterFish
from project.fish.freshwater_fish import FreshwaterFish
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.decoration.decoration_repository import DecorationRepository


class Controller:
    __AQUARIUMS_MAPPER = {
        "SaltwaterAquarium": SaltwaterAquarium,
        "FreshwaterAquarium": FreshwaterAquarium,
    }
    __DECORATION_MAPPER = {
        "Plant": Plant,
        "Ornament": Ornament,
    }
    __FISH_MAPPER = {
        "SaltwaterFish": SaltwaterFish,
        "FreshwaterFish": FreshwaterFish,
    }

    def __init__(self) -> None:
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str) -> str:
        if aquarium_type not in self.__AQUARIUMS_MAPPER:
            return f"Invalid aquarium type."

        aquarium = self.__AQUARIUMS_MAPPER[aquarium_type](aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str) -> str:
        if decoration_type not in self.__DECORATION_MAPPER:
            return f"Invalid decoration type."

        decoration = self.__DECORATION_MAPPER[decoration_type]()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str) -> str:
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "none":
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self._find_aquarium_by_name(aquarium_name)
        if aquarium is not None:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float) -> str:
        if fish_type not in self.__FISH_MAPPER:
            return f"There isn't a fish of type {fish_type}."

        fish = self.__FISH_MAPPER[fish_type](fish_name, fish_species, price)
        aquarium = self._find_aquarium_by_name(aquarium_name)
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str) -> str:
        aquarium = self._find_aquarium_by_name(aquarium_name)
        return f"Fish fed: {aquarium.feed()}"

    def calculate_value(self, aquarium_name: str) -> str:
        aquarium = self._find_aquarium_by_name(aquarium_name)
        value = aquarium.calculate_value()
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self) -> str:
        info = [str(aquarium) for aquarium in self.aquariums]
        return '\n'.join(info)

    def _find_aquarium_by_name(self, aquarium_name: str):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
