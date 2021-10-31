class Trainer:
    id = 1

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def get_next_id(cls):
        cls.id += 1
        return cls.id - 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
