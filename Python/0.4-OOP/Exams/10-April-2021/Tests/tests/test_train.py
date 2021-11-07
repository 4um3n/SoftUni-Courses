from project.train.train import Train
from unittest import TestCase, main


class TrainTests(TestCase):
    def setUp(self) -> None:
        self.train = Train("name", 10)

    def test_init_train(self) -> None:
        self.assertEqual("name", self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertListEqual([], self.train.passengers)

    def test_add_passenger_train_full_raises(self) -> None:
        self.train.passengers = ["test"] * 10
        with self.assertRaises(ValueError) as ex:
            self.train.add("name")
        self.assertEqual(f"Train is full", str(ex.exception))

    def test_add_passenger_exists_raises(self) -> None:
        result = self.train.add("name")
        self.assertEqual(f"Added passenger name", result)
        self.assertListEqual(["name"], self.train.passengers)
        with self.assertRaises(ValueError) as ex:
            self.train.add("name")
        self.assertEqual(f"Passenger name Exists", str(ex.exception))

    def test_remove_passenger_not_found_raises(self) -> None:
        self.train.passengers = ["name"]
        result = self.train.remove("name")
        self.assertEqual(f"Removed name", result)
        self.assertListEqual([], self.train.passengers)
        with self.assertRaises(ValueError) as ex:
            self.train.remove("name")
        self.assertEqual(f"Passenger Not Found", str(ex.exception))


if __name__ == '__main__':
    main()
