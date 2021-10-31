class Category:
    def __init__(self, self_id: int, name: str):
        self.id = self_id
        self.name = name

    def edit(self, new_name: str):
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"
