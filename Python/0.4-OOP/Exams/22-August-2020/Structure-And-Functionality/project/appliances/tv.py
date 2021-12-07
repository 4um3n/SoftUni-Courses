from project.appliances.appliance import Appliance


class TV(Appliance):
    __DEFAULT_COST = 1.5

    def __init__(self):
        super().__init__(self.__DEFAULT_COST)
