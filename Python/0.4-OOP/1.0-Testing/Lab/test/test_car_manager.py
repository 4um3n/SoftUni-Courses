from project.car import Car
from unittest import TestCase, main


class CarTests(TestCase):
    def setUp(self) -> None:
        self.car = Car("make", "model", 5, 10)

    def test_init_car(self):
        self.assertEqual("make", self.car.make)
        self.assertEqual("model", self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(10, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_car(self):
        self.car.make = "new make"
        self.assertEqual("new make", self.car.make)
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual(f"Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_car(self):
        self.car.model = "new model"
        self.assertEqual("new model", self.car.model)
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual(f"Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter_car(self):
        self.car.fuel_consumption = 10
        self.assertEqual(10, self.car.fuel_consumption)
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual(f"Fuel consumption cannot be zero or negative!", str(ex.exception))
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual(f"Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_car(self):
        self.car.fuel_capacity = 30
        self.assertEqual(30, self.car.fuel_capacity)
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual(f"Fuel capacity cannot be zero or negative!", str(ex.exception))
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual(f"Fuel capacity cannot be zero or negative!", str(ex.exception))
    
    def test_fuel_amount_setter_car(self):
        self.car.fuel_amount = 10
        self.assertEqual(10, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual(f"Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_method_car(self):
        self.car.refuel(5)
        self.assertEqual(5, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual(f"Fuel amount cannot be zero or negative!", str(ex.exception))
        self.car.refuel(30)
        self.assertEqual(10, self.car.fuel_amount)

    def test_drive_method_car(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual(f"You don't have enough fuel to drive!", str(ex.exception))
        self.car.fuel_amount = 6
        self.car.drive(100)
        self.assertEqual(1, self.car.fuel_amount)


if __name__ == '__main__':
    main()
