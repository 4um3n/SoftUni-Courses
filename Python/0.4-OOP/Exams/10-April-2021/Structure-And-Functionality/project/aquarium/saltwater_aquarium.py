from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    __DEFAULT_CAPACITY = 25

    def __init__(self, name: str) -> None:
        super().__init__(name, self.__DEFAULT_CAPACITY)
