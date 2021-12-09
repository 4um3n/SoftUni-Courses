from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    __INITIAL_SIZE = 3
    __SIZE_GAIN_VALUE = 3
    __TYPE = "FreshwaterFish"

    def __init__(self, name: str, species: str, price: float) -> None:
        super().__init__(name, species, self.__INITIAL_SIZE, price)

    @property
    def fish_type(self):
        return self.__TYPE

    def eat(self) -> None:
        self.size += self.__SIZE_GAIN_VALUE
