from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    __INITIAL_SIZE = 5
    __SIZE_GAIN_VALUE = 2
    __TYPE = "SaltwaterFish"

    def __init__(self, name: str, species: str, price: float) -> None:
        super().__init__(name, species, self.__INITIAL_SIZE, price)

    @property
    def fish_type(self):
        return self.__TYPE

    def eat(self) -> None:
        self.size += self.__SIZE_GAIN_VALUE
