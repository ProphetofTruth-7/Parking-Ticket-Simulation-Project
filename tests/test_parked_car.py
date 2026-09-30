#Unittest File for parked_car.py

import unittest
from parked_car import ParkedCar
from unittest.mock import patch


class TestParkedCar(unittest.TestCase):
    def setUp(self):
        self.parked_car = ParkedCar("Toyota", "Solara", "Ruby Red", "Chasin", 60)

    def test_valid_access(self):
        self.assertEqual(self.parked_car.make, "Toyota")
        self.assertEqual(self.parked_car.model, "Solara")
        self.assertEqual(self.parked_car.color, "Ruby Red")
        self.assertEqual(self.parked_car.license_number, "Chasin")
        self.assertEqual(self.parked_car.minutes_parked, 60)
    def test_valid_assignment(self):
        self.parked_car.make = "Honda"
        self.parked_car.model = "Civic"
        self.parked_car.color = "Blue"
        self.parked_car.license_number = "Runnin"
        self.parked_car.minutes_parked = 30
        self.assertEqual(self.parked_car.make, "Honda")
        self.assertEqual(self.parked_car.model, "Civic")
        self.assertEqual(self.parked_car.color, "Blue")
        self.assertEqual(self.parked_car.license_number, "Runnin")
        self.assertEqual(self.parked_car.minutes_parked, 30)

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            ParkedCar("", "Solara", "Ruby Red", "Chasin", 60)

    def test_invalid_string(self):
        with self.assertRaises(ValueError):
            ParkedCar(123, "Solara", "Ruby Red", "Chasin", 60)

    def test_invalid_minutes_negative(self):
        with self.assertRaises(ValueError):
            ParkedCar("Toyota", "Solara", "Ruby Red", "Chasin", -65)
    def test_invalid_minutes_float(self):
        with self.assertRaises(ValueError):
            ParkedCar("Toyota", "Solara", "Ruby Red", "Chasin", 55.4)
    def test_zero_minutes(self):
        self.parked_car = ParkedCar("Toyota", "Solara", "Ruby Red", "Chasin", 0)
        self.assertEqual(self.parked_car.minutes_parked, 0)
    def test_valid_minutes(self):
        self.parked_car = ParkedCar("Toyota", "Solara", "Ruby Red", "Chasin", 60)
        self.assertEqual(self.parked_car.minutes_parked, 60)

                          

if __name__ == "__main__":
    unittest.main()