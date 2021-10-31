from collections import defaultdict


class Shop:
    def __init__(self, name: str, self_type: str, capacity: int):
        self.name = name
        self.type = self_type
        self.capacity = capacity
        self.items = defaultdict(lambda: 0)

    @classmethod
    def small_shop(cls, name: str, self_type: str):
        return cls(name, self_type, 10)

    def add_item(self, item_name: str):
        if sum(self.items.values()) < self.capacity:
            self.items[item_name] += 1
            return f"{item_name} added to the shop"

        return f"Not enough capacity in the shop"

    def remove_item(self, item_name: str, amount: int):
        if self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
