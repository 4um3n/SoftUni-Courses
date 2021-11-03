from project.mammal import Mammal
from unittest import TestCase, main


class MammalTests(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("name", "type", "sound")

    def test_init_mammal(self):
        self.assertEqual("name", self.mammal.name)
        self.assertEqual("type", self.mammal.type)
        self.assertEqual("sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_mammal(self):
        result = self.mammal.make_sound()
        self.assertEqual(f"name makes sound", result)

    def test_get_kingdom_mammal(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info_mammal(self):
        result = self.mammal.info()
        self.assertEqual(f"name is of type type", result)


if __name__ == '__main__':
    main()
