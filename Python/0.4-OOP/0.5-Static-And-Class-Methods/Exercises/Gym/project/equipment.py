class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.get_next_id()

    @classmethod
    def get_next_id(cls):
        cls.id += 1
        return cls.id - 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"


