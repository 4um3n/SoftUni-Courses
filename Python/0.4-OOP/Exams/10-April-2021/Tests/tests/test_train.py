from project.train.train import Train
from unittest import  TestCase, main


class TrainTests(TestCase):
    def setUp(self) -> None:
        self.train = Train("Test", 2)

    def test_structure_initialization(self):
        self.assertEqual("Test", self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertListEqual([], self.train.passengers)

    def test_add_passenger_not_enough_capacity_raises(self):
        self.train.passengers = ["FIRST", "SECOND"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("Test")
        expected = f"Train is full"
        self.assertEqual(expected, str(ex.exception))
    
    def test_add_passenger_exist_raises(self):
        self.assertListEqual([], self.train.passengers)
        result = self.train.add("Passenger")
        expected = f"Added passenger Passenger"
        self.assertEqual(expected, result)
        self.assertListEqual(["Passenger"], self.train.passengers)
        with self.assertRaises(ValueError) as ex:
            self.train.add("Passenger")
        expected = f"Passenger Passenger Exists"
        self.assertEqual(expected, str(ex.exception))

    def test_remove_passenger_not_found_raises(self):
        self.train.add("Passenger")
        result = self.train.remove("Passenger")
        expected = f"Removed Passenger"
        self.assertEqual(expected, result)
        with self.assertRaises(ValueError) as ex:
            self.train.remove("Passenger")
        expected = f"Passenger Not Found"
        self.assertEqual(expected, str(ex.exception))


if __name__ == '__main__':
    main()
