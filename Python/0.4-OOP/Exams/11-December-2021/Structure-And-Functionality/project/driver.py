class Driver:
    def __init__(self, name: str) -> None:
        self.name = name
        self.car = None
        self.number_of_wins: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(f"Name should contain at least one character!")
        self.__name = value
