import unittest
from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(12.5, 150.3)

    def test_correct_initialization(self):
        self.assertEqual(self.vehicle.fuel, 12.5)
        self.assertEqual(self.vehicle.horse_power, 150.3)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_working_properly(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 0)

    def test_drive_error_working_properly(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(19)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_working_properly(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(10.5)
        self.assertEqual(self.vehicle.fuel, 10.5)

    def test_refuel_exception_working_properly(self):
        self.vehicle.drive(10)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(13)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_method_working_properly(self):
        result = self.vehicle.__str__()
        expected_result = f"The vehicle has {150.3} " \
                          f"horse power with {12.5} fuel left and {1.25} fuel consumption"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
