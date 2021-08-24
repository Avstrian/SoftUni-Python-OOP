from collections import defaultdict


class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = defaultdict(lambda: 0)

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if self.capacity == 0:
            return "Not enough capacity in the shop"
        self.items[item_name] += 1
        self.capacity -= 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name, amount):
        if item_name in self.items:
            if self.items[item_name] - amount >= 0:
                self.items[item_name] -= amount
                self.capacity += amount
                return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
