from project.integer_list import IntegerList
from unittest import TestCase, main


class ListTests(TestCase):
    def setUp(self) -> None:
        self.integer_list = IntegerList(1, 2.2, 0, -1, -2.2, 'asd', True, None)

    def test_init_integer_list(self):
        self.assertListEqual([1, 0, -1], self.integer_list.get_data())

    def test_integer_list_add_method(self):
        result = self.integer_list.add(2)
        self.assertListEqual([1, 0, -1, 2], result)
        for value in [2.2, -2.2, True, None, 'asd']:
            with self.assertRaises(ValueError) as ex:
                self.integer_list.add(value)

            self.assertEqual(f"Element is not Integer", str(ex.exception))

    def test_integer_list_remove_index_method(self):
        self.assertListEqual([1, 0, -1], self.integer_list.get_data())
        result = self.integer_list.remove_index(0)
        self.assertEqual(1, result)
        self.assertListEqual([0, -1], self.integer_list.get_data())
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(3)

        self.assertEqual(f"Index is out of range", str(ex.exception))

    def test_integer_list_get_method(self):
        result = self.integer_list.get(0)
        self.assertEqual(1, result)
        self.assertListEqual([1, 0, -1], self.integer_list.get_data())
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(3)

        self.assertEqual(f"Index is out of range", str(ex.exception))

    def test_integer_list_insert_method(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(3, 3)

        self.assertEqual(f"Index is out of range", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(1, 3.3)

        self.assertEqual(f"Element is not Integer", str(ex.exception))
        self.integer_list.insert(0, 2)
        self.assertListEqual([2, 1, 0, -1], self.integer_list.get_data())

    def test_integer_list_get_biggest_method(self):
        temp_list = IntegerList(1, 2, 3, 3, 3)
        result = temp_list.get_biggest()
        self.assertEqual(3, result)

    def test_integer_list_get_index_method(self):
        temp_list = IntegerList(1, 2, 3, 3, 3)
        result = temp_list.get_index(3)
        self.assertEqual(2, result)


if __name__ == '__main__':
    main()
