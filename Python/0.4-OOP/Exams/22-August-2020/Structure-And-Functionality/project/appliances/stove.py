from project.appliances.appliance import Appliance


class Stove(Appliance):
    __DEFAULT_APPLIANCE_COST = 0.7

    def __init__(self) -> None:
        super().__init__(self.__DEFAULT_APPLIANCE_COST)
