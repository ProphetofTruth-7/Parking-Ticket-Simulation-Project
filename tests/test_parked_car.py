#Unittest File for parked_car.py

import unittest
from parked_car import ParkedCar
from unittest.mock import patch


class TestParkedCar(unittest.TestCase):
    def test_default_constructor(self):
        self.assertEqual(Date().alphabetic_return(), "January 01, 1900")
    def test_valid_constructor(self):
        self.assertEqual(Date(2026, 9, 14).alphabetic_return(), "September 14, 2026")
    def setUp(self):
        self.date = Date(2026, 9, 13)
        self.datebefore = Date(2026, 8, 4)

                                                         # Part 2 Tests
# Subtraction Tests
    def test_subtraction_basic(self):
        self.assertEqual(self.date - self.datebefore, 40)
        self.assertEqual(self.date - self.dateafter, -43)
        self.assertEqual(self.date - self.date, 0)
        self.assertEqual(self.date - self.dateleap, 927)
    def test_subtraction_invalid_type(self):
        with self.assertRaises(TypeError):
            self.date - 5
# Decrement Tests
    def test_decrement_single(self):
        self.date.decrement()
        self.assertEqual(self.date.alphabetic_return(), "September 12, 2026")
# Input() Tests
    @patch("builtins.input", side_effect=["2026", "9", "13"])  #No clue why its written like this, but it basically mimicks a user inputting month(4), day(18), and year(2018)
    def test_input_valid(self, mock_input):
        result = Date.from_input()
        self.assertEqual(result.month, 9)
        self.assertEqual(result.day, 13)
        self.assertEqual(result.year, 2026)
# Invalid Value Tests
    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            Date(1900, 13, 1)
#Setter Tests
    def test_set_date(self):
        self.date.set_date(2007, 4, 2)
        self.assertEqual(self.date.alphabetic_return(), "April 02, 2007")
    def test_set_invalid_date(self):
        with self.assertRaises(ValueError):
            self.date.set_date(2007, 4, 60)

if __name__ == "__main__":
    unittest.main()