from project.car import Car


class FamilyCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = FamilyCar.DEFAULT_FUEL_CONSUMPTION
