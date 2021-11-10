from project.factory.paint_factory import PaintFactory
from unittest import TestCase, main


class PaintFactoryTests(TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory("name", 10)

    def test_init_setup(self):
        self.assertEqual("name", self.paint_factory.name)
        self.assertEqual(10, self.paint_factory.capacity)
        self.assertDictEqual({}, self.paint_factory.ingredients)
        expected = ["white", "yellow", "blue", "green", "red"]
        self.assertListEqual(expected, self.paint_factory.valid_ingredients)

    def test_abstract_methods_existing(self):
        self.assertTrue("add_ingredient" in dir(PaintFactory))
        self.assertTrue("remove_ingredient" in dir(PaintFactory))
        self.assertTrue("__init__" in dir(PaintFactory))

    def test_product_property_returns_correct(self):
        result = self.paint_factory.products
        expected = self.paint_factory.ingredients
        self.assertDictEqual(expected, result)

    def test_add_ingredient_not_enough_space_raises(self):
        self.paint_factory.add_ingredient("white", 5)
        expected = {"white": 5}
        self.assertDictEqual(expected, self.paint_factory.ingredients)
        self.paint_factory.add_ingredient("white", 5)
        expected = {"white": 10}
        self.assertDictEqual(expected, self.paint_factory.ingredients)

        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient("white", 1)
        self.assertEqual(f"Not enough space in factory", str(ex.exception))

    def test_add_ingredient_not_allowed_product_type_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient("purple", 5)
        self.assertEqual(f"Ingredient of type purple not allowed in PaintFactory", str(ex.exception))

    def test_remove_ingredient_cannot_be_negative_quantity_raises(self):
        self.paint_factory.ingredients = {"white": 10}
        self.paint_factory.remove_ingredient("white", 5)
        expected = {"white": 5}
        self.assertDictEqual(expected, self.paint_factory.ingredients)

        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient("white", 6)
        self.assertEqual(f"Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_no_such_ingredient_raises(self):
        self.assertDictEqual({}, self.paint_factory.ingredients)
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient("white", 0)
        self.assertEqual(f"'No such ingredient in the factory'", str(ex.exception))

    def test_can_add(self):
        self.assertTrue(self.paint_factory.can_add(10))
        self.paint_factory.add_ingredient("white", 5)
        self.assertFalse(self.paint_factory.can_add(10))

    def test_paint_factory_representation(self):
        result = repr(self.paint_factory)
        expected = f"Factory name: name with capacity 10.\n"
        self.assertEqual(expected, result)
        self.paint_factory.add_ingredient("white", 10)
        result = repr(self.paint_factory)
        expected = f"Factory name: name with capacity 10.\n" \
                   f"white: 10\n"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()


