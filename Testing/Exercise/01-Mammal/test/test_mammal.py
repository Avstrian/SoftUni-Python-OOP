import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "Test_type", "Test_sound")

    def test_mammal_is_initialized_correctly(self):
        self.assertEqual(self.mammal.name, "Test")
        self.assertEqual(self.mammal.type, "Test_type")
        self.assertEqual(self.mammal.sound, "Test_sound")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound_working_properly(self):
        result = self.mammal.make_sound()
        expected_result = "Test makes Test_sound"
        self.assertEqual(result, expected_result)

    def test_get_kingdom_working_properly(self):
        kingdom = self.mammal.get_kingdom()
        self.assertEqual("animals", kingdom)

    def test_info_working_properly(self):
        result = self.mammal.info()
        expected_result = "Test is of type Test_type"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()