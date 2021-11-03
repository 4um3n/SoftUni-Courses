from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTests(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(50.0, 100.0)

    def test_init_vehicle(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_instance_attributes_type(self):
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertTrue(isinstance(self.vehicle.fuel_consumption, float))
        self.assertTrue(isinstance(self.vehicle.capacity, float))
        self.assertTrue(isinstance(self.vehicle.horse_power, float))

    def test_drive_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)

        self.assertEqual(f"Not enough fuel", str(ex.exception))
        self.vehicle.fuel = 125
        self.vehicle.drive(100)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_too_much_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.assertEqual(50, self.vehicle.fuel)
            self.vehicle.refuel(1)

        self.assertEqual(f"Too much fuel", str(ex.exception))

        self.vehicle.fuel = 10
        self.vehicle.refuel(40)
        self.assertEqual(50, self.vehicle.fuel)

    def test_str_method_returns_proper(self):
        result = str(self.vehicle)
        expected = f"The vehicle has 100.0 " \
                   f"horse power with 50.0 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
