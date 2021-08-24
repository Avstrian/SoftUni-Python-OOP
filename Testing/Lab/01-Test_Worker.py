import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy == 0:
            raise Exception("Not enough energy.")
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} has saved {self.money} money."


class WorkerTests(unittest.TestCase):
    def test_person_is_initialized_correctly(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual(worker.name, "Test")
        self.assertEqual(worker.salary, 100)
        self.assertEqual(worker.energy, 10)
        self.assertEqual(worker.money, 0)

    def test_worker_energy_increased_after_rest(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual(worker.energy, 10)
        worker.rest()
        self.assertEqual(worker.energy, 11)

    def test_if_working_with_negative_energy(self):
        worker = Worker("Test", 100, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_money_increase_after_work(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual(0, worker.money)
        worker.work()
        self.assertEqual(100, worker.money)

    def test_worker_energy_decrease_after_work(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual(10, worker.energy)
        worker.work()
        self.assertEqual(9, worker.energy)

    def test_get_info_method(self):
        worker = Worker("Test", 100, 10)
        result = worker.get_info()
        expected_result = f"Test has saved 0 money."
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
