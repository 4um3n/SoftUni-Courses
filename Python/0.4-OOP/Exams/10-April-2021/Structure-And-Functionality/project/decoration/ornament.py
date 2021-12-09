from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    __COMFORT = 1
    __PRICE = 5

    def __init__(self):
        super().__init__(self.__COMFORT, self.__PRICE)
