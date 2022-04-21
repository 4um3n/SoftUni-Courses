from project.appliances.appliance import Appliance


class Stove(Appliance):
    __DEFAULT_COST = 0.7

    def __init__(self):
        super().__init__(self.__DEFAULT_COST)
