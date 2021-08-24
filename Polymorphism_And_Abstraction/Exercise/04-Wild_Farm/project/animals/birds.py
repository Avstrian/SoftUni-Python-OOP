from project.animals.animal import Bird


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.food_eaten = 0

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if type(food).__name__ == "Meat":
            self.food_eaten += food.quantity
            self.weight += 0.25 * food.quantity
        else:
            return f"Owl does not eat {type(food).__name__}!"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.food_eaten = 0

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += 0.35 * food.quantity
