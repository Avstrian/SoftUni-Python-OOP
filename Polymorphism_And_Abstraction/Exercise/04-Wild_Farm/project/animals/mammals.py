from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if type(food).__name__ == "Vegetable" or type(food).__name__ == "Fruit":
            self.food_eaten += food.quantity
            self.weight += 0.10 * food.quantity
        else:
            return f"Mouse does not eat {type(food).__name__}!"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if type(food).__name__ == "Meat":
            self.food_eaten += food.quantity
            self.weight += 0.40 * food.quantity
        else:
            return f"Dog does not eat {type(food).__name__}!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if type(food).__name__ == "Vegetable" or type(food).__name__ == "Meat":
            self.food_eaten += food.quantity
            self.weight += 0.30 * food.quantity
        else:
            return f"Cat does not eat {type(food).__name__}!"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if type(food).__name__ == "Meat":
            self.food_eaten += food.quantity
            self.weight += 1.00 * food.quantity
        else:
            return f"Tiger does not eat {type(food).__name__}!"
