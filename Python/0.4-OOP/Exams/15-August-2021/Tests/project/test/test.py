from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTests(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("name")

    def test_init_pet_shop(self):
        self.assertEqual("name", self.pet_shop.name)
        self.assertDictEqual({}, self.pet_shop.food)
        self.assertListEqual([], self.pet_shop.pets)

    def test_add_food_negative_or_zero_quantity_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("name", 0)

        self.assertEqual(f"Quantity cannot be equal to or less than 0", str(ex.exception))

    def test_add_food_success(self):
        result = self.pet_shop.add_food("name", 10)
        self.assertDictEqual({"name": 10}, self.pet_shop.food)
        self.assertEqual(f"Successfully added 10.00 grams of name.", result)

    def test_add_pet_cannot_add_same_name_raises(self):
        self.pet_shop.pets.append("name")
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("name")

        self.assertEqual(f"Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_success(self):
        result = self.pet_shop.add_pet("name")
        self.assertListEqual(["name"], self.pet_shop.pets)
        self.assertEqual(f"Successfully added name.", result)

    def test_feed_pet_invalid_pet_name_raises(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("food", "name")

        self.assertEqual(f"Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_food_not_in_foods(self):
        self.pet_shop.pets.append("name")
        result = self.pet_shop.feed_pet("food", "name")
        self.assertEqual(f"You do not have food", result)

    def test_feed_pet_food_under_100(self):
        self.pet_shop.pets = ["name"]
        self.pet_shop.food = {"food": 99}
        result = self.pet_shop.feed_pet("food", "name")
        self.assertDictEqual({"food": 1099.00}, self.pet_shop.food)
        self.assertEqual(f"Adding food...", result)

    def test_feed_pet_success(self):
        self.pet_shop.pets = ["name"]
        self.pet_shop.food = {"food": 100}
        result = self.pet_shop.feed_pet("food", "name")
        self.assertDictEqual({"food": 0}, self.pet_shop.food)
        self.assertEqual(f"name was successfully fed", result)

    def test_repr_pet_shop(self):
        self.pet_shop.pets = ["pet", "pet1", "pet2"]
        result = repr(self.pet_shop)
        expected = f'Shop name:\n' \
                   f'Pets: pet, pet1, pet2'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
