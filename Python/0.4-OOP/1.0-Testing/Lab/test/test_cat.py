from project.cat import Cat
from unittest import TestCase, main


class CateTests(TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Test")

    def test_cat_size_increased_after_eating(self):
        self.assertEqual(0, self.cat.size)
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_is_fed_after_eating(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_fed(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual(f"Already fed.", str(ex.exception))

    def test_cat_cannot_sleep_if_not_fed(self):
        self.assertFalse(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual(f"Cannot sleep while hungry", str(ex.exception))

    def test_cat_not_sleepy_after_sleep(self):
        self.assertFalse(self.cat.sleepy)
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
