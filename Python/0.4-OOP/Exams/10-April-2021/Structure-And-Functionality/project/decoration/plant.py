from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    __COMFORT = 5
    __PRICE = 10

    def __init__(self):
        super().__init__(self.__COMFORT, self.__PRICE)
