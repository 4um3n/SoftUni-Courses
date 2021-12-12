from project.car.car import Car


class SportsCar(Car):
    __MIN_SPEED_LIMIT = 400
    __MAX_SPEED_LIMIT = 600
    __TYPE = "SportsCar"

    @property
    def car_type(self):
        return self.__TYPE

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value not in range(self.__MIN_SPEED_LIMIT, self.__MAX_SPEED_LIMIT + 1):
            error_text = f"Invalid speed limit! Must be between {self.__MIN_SPEED_LIMIT} and {self.__MAX_SPEED_LIMIT}!"
            raise ValueError(error_text)
        self.__speed_limit = value
