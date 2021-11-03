from project.hero import Hero
from unittest import TestCase, main


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("hero_username", 1, 50.0, 25.0)
        self.enemy = Hero("enemy_enemy", 1, 50.0, 25.0)

    def test_init_hero(self):
        self.assertEqual("hero_username", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(50.0, self.hero.health)
        self.assertEqual(25.0, self.hero.damage)

    def test_instance_attributes_types(self):
        self.assertTrue(isinstance(self.hero.username, str))
        self.assertTrue(isinstance(self.hero.level, int))
        self.assertTrue(isinstance(self.hero.health, float))
        self.assertTrue(isinstance(self.hero.damage, float))

    def test_battle_enemy_username_equals_hero_name_raises(self):
        self.enemy.username = self.hero.username
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_lower_than_or_equals_zero_raises(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(f"Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_lower_than_or_equals_zero_raises(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_enemy_wins(self):
        battle_result = self.hero.battle(self.enemy)
        self.assertEqual(25.0, self.hero.health)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(30.0, self.enemy.health)
        self.assertEqual(30.0, self.enemy.damage)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(f"You lose", battle_result)

    def test_battle_hero_wins(self):
        self.enemy.health = 25.0
        battle_result = self.hero.battle(self.enemy)
        self.assertEqual(0.0, self.enemy.health)
        self.assertEqual(1, self.enemy.level)
        self.assertEqual(30.0, self.hero.health)
        self.assertEqual(30.0, self.hero.damage)
        self.assertEqual(f"You win", battle_result)

    def test_battle_draw(self):
        self.hero.health = 25.0
        self.enemy.health = 25.0
        battle_result = self.hero.battle(self.enemy)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(1, self.enemy.level)
        self.assertEqual(25.0, self.hero.damage)
        self.assertEqual(25.0, self.enemy.damage)
        self.assertEqual(0.0, self.hero.health)
        self.assertEqual(0.0, self.enemy.health)
        self.assertEqual(f"Draw", battle_result)

    def test_hero_string_method_returns_proper(self):
        result = str(self.hero)
        expected = f"Hero hero_username: 1 lvl\n" \
                   f"Health: 50.0\n" \
                   f"Damage: 25.0\n"

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
