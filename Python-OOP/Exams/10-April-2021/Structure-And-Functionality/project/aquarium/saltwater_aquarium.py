from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    __CAPACITY = 25
    __FISH_TYPE = "SaltwaterFish"

    def __init__(self, name: str) -> None:
        super().__init__(name, self.__CAPACITY)

    def add_fish(self, fish) -> str:
        if not self._can_add_fish():
            return f"Not enough capacity."

        if self.__FISH_TYPE != fish.fish_type:
            return f"Water not suitable."

        self.fish.append(fish)
        return f"Successfully added {self.__FISH_TYPE} to {self.name}."
