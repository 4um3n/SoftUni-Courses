from project.appliances.appliance import Appliance


class Fridge(Appliance):
    __DEFAULT_COST = 1.2

    def __init__(self) -> None:
        super().__init__(self.__DEFAULT_COST)
