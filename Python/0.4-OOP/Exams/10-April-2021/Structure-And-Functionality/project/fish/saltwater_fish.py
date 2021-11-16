from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    AQUARIUM = "SaltwaterAquarium"
    FISH_SIZE_INCREASING_VALUE = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name=name, species=species, size=5, price=price)

    def eat(self):
        self.size += self.FISH_SIZE_INCREASING_VALUE
