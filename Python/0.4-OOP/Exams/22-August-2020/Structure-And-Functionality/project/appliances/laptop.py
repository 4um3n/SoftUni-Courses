from project.appliances.appliance import Appliance


class Laptop(Appliance):
    __DEFAULT_COST = 1

    def __init__(self):
        super().__init__(self.__DEFAULT_COST)
