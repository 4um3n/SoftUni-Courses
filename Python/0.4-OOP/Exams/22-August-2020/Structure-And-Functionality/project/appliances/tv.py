from project.appliances.appliance import Appliance


class TV(Appliance):
    __DEFAULT_APPLIANCE_COST = 1.5

    def __init__(self) -> None:
        super().__init__(self.__DEFAULT_APPLIANCE_COST)
