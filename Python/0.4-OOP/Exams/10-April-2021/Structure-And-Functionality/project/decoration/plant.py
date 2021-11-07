from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    __DEFAULT_COMFORT = 5
    __DEFAULT_PRICE = 10

    def __init__(self):
        super().__init__(self.__DEFAULT_COMFORT, self.__DEFAULT_PRICE)
