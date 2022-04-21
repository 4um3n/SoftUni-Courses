class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget < price:
                return f"Not enough budget"

            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {type(animal).__name__} added to the zoo"

        return f"Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"

        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = sum([w.salary for w in self.workers])
        if self.__budget < needed_money:
            return f"You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed_money
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_money = sum([a.money_for_care for a in self.animals])
        if self.__budget < needed_money:
            return f"You have no budget to tend the animals. They are unhappy."

        self.__budget -= needed_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions_count, tigers_count, cheetah_count = 0, 0, 0
        lions_info, tigers_info, cheetah_info = [], [], []

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions_count += 1
                lions_info.append(animal.__repr__())

            elif animal.__class__.__name__ == "Tiger":
                tigers_count += 1
                tigers_info.append(animal.__repr__())

            elif animal.__class__.__name__ == "Cheetah":
                cheetah_count += 1
                cheetah_info.append(animal.__repr__())

        info = [f"You have {len(self.animals)} animals", f"----- {lions_count} Lions:"]
        info.extend(lions_info)
        info.append(f"----- {tigers_count} Tigers:")
        info.extend(tigers_info)
        info.append(f"----- {cheetah_count} Cheetahs:")
        info.extend(cheetah_info)
        return '\n'.join(info)

    def workers_status(self):
        info = [f"You have {len(self.workers)} workers"]

        keepers_count, caretakers_count, vets_count = 0, 0, 0
        keepers_info, caretakers_info, vets_info = [], [], []

        for worker in self.workers:
            if type(worker).__name__ == "Keeper":
                keepers_count += 1
                keepers_info.append(worker.__repr__())

            elif type(worker).__name__ == "Caretaker":
                caretakers_count += 1
                caretakers_info.append(worker.__repr__())

            elif type(worker).__name__ == "Vet":
                vets_count += 1
                vets_info.append(worker.__repr__())

        info = [f"You have {len(self.workers)} workers", f"----- {keepers_count} Keepers:"]
        info.extend(keepers_info)
        info.append(f"----- {caretakers_count} Caretakers:")
        info.extend(caretakers_info)
        info.append(f"----- {vets_count} Vets:")
        info.extend(vets_info)
        return '\n'.join(info)
