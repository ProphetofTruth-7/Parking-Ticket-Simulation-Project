import unittest
from parking_meter import ParkingMeter

class TestParkingMeter(unittest.TestCase):
    def setUp(self):
        self.parking_meter = ParkingMeter(60)

    def test_valid_access(self):
        self.assertEqual(self.parking_meter.purchased_parking, 60)
    def test_valid_assignment(self):
        self.parking_meter.purchased_parking = 30
        self.assertEqual(self.parking_meter.purchased_parking, 30)

    def test_invalid_purchased_minutes_negative(self):
        with self.assertRaises(ValueError):
            ParkingMeter(-60)
    def test_invalid_purchased_minutes_float(self):
        with self.assertRaises(ValueError):
            ParkingMeter(60.4)
    def test_zero_purchased_minutes(self):
        self.parking_meter = ParkingMeter(0)
        self.assertEqual(self.parking_meter.purchased_parking, 0)
    def test_valid_purchased_minutes(self):
        self.parking_meter = ParkingMeter(50)
        self.assertEqual(self.parking_meter.purchased_parking, 50)

if __name__ == "__main__":
    unittest.main()