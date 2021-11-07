from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    __DEFAULT_COMFORT = 1
    __DEFAULT_PRICE = 5

    def __init__(self):
        super().__init__(self.__DEFAULT_COMFORT, self.__DEFAULT_PRICE)
