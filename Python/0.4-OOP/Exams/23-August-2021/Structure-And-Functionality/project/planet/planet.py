class Planet:
    def __init__(self, name: str) -> None:
        self.name = name
        self.items = []

    @property
    def name(self) -> property:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        if not value or value == ' ':
            raise ValueError(f"Planet name cannot be empty string or whitespace!")

        self.__name = value
