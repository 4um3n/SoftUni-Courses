class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, name):
        if len(Vet.animals) < Vet.space:
            Vet.animals.append(name)
            self.animals.append(name)
            return f"{name} registered in the clinic"

        return f"Not enough space"

    def unregister_animal(self, name):
        if name in self.animals:
            Vet.animals.remove(name)
            self.animals.remove(name)
            return f"{name} unregistered successfully"

        return f"{name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic"

