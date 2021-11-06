from project.appliances.appliance import Appliance


class Laptop(Appliance):
    __DEFAULT_APPLIANCE_COST = 1

    def __init__(self) -> None:
        super().__init__(self.__DEFAULT_APPLIANCE_COST)

