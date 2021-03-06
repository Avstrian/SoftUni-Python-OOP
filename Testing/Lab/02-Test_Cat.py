import unittest


class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Test")

    def test_cat_size_increased_after_eating(self):
        self.assertEqual(0, self.cat.size)
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_fed_after_eating(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_eat_after_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_sleep_before_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()
