import unittest
from project.hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Test", 1, 100, 10)

    def test_correct_initialization(self):
        self.assertEqual(self.hero.username, "Test")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 10)

    def test_not_able_to_fight_yourself(self):
        enemy = Hero("Test", 1, 100, 10)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_not_able_to_fight_with_no_health(self):
        self.hero.health -= 100
        enemy = Hero("Enemy", 1, 100, 10)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_not_able_to_fight_enemy_with_no_health(self):
        enemy = Hero("Enemy", 1, 0, 10)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)

        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ex.exception))

    def test_draw_working_properly(self):
        enemy = Hero("Enemy", 1, 10, 100)
        self.assertEqual("Draw", self.hero.battle(enemy))

    def test_win_working_properly(self):
        enemy = Hero("Enemy", 1, 10, 90)
        self.assertEqual("You win", self.hero.battle(enemy))

    def test_stat_increase_after_winning(self):
        enemy = Hero("Enemy", 1, 10, 90)
        self.hero.battle(enemy)
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 15)
        self.assertEqual(self.hero.damage, 15)

    def test_lose_working_properly(self):
        self.hero.damage -= 10
        enemy = Hero("Enemy", 1, 10, 90)
        self.assertEqual("You lose", self.hero.battle(enemy))

    def test_stat_increase_after_losing(self):
        enemy = Hero("Enemy", 1, 100, 900)
        self.hero.battle(enemy)
        self.assertEqual(enemy.level, 2)
        self.assertEqual(enemy.health, 95)
        self.assertEqual(enemy.damage, 905)

    def test_str_working_properly(self):
        result = self.hero.__str__()
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
