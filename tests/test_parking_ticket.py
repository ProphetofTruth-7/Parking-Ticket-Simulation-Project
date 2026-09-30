import unittest
from unittest.mock import Mock
from parking_ticket import ParkingTicket


class TestParkingTicket(unittest.TestCase):
    def setUp(self):
        car = Mock(make="Jeep", model="Cherokee", color="Black", license_number="Honse9", minutes_parked=120)
        meter = Mock(purchased_parking=60)
        officer = Mock()
        officer.name = "Randall Griggs"
        officer.badge_number = "A2599"
        officer.car = car
        officer.meter = meter
        self.parking_ticket = ParkingTicket(officer, 0)

    def test_calculate_fine_121(self):
        self.parking_ticket.officer.car.minutes_parked = 181
        fine = self.parking_ticket.calculate_fine()
        self.assertEqual(fine, 45)
    def test_calculate_fine_120(self):
        self.parking_ticket.officer.car.minutes_parked = 180
        fine = self.parking_ticket.calculate_fine()
        self.assertEqual(fine, 35)
    def test_calculate_fine_61(self):
        self.parking_ticket.officer.car.minutes_parked = 121
        fine = self.parking_ticket.calculate_fine()
        self.assertEqual(fine, 35)
    def test_calculate_fine_60(self):
        self.parking_ticket.officer.car.minutes_parked = 120
        fine = self.parking_ticket.calculate_fine()
        self.assertEqual(fine, 25)
    def test_calculate_fine_1(self):
        self.parking_ticket.officer.car.minutes_parked = 61
        fine = self.parking_ticket.calculate_fine()
        self.assertEqual(fine, 25)

    def test_correct_officer_info(self):
        self.assertEqual(self.parking_ticket.officer.name, "Randall Griggs")
        self.assertEqual(self.parking_ticket.officer.badge_number, "A2599")
    def test_correct_car_info(self):
        self.assertEqual(self.parking_ticket.officer.car.make, "Jeep")
        self.assertEqual(self.parking_ticket.officer.car.model, "Cherokee")
        self.assertEqual(self.parking_ticket.officer.car.color, "Black")
        self.assertEqual(self.parking_ticket.officer.car.license_number, "Honse9")

    def test_constructor_violation(self):
        self.parking_ticket.officer.car.minutes_parked = 60
        with self.assertRaises(ValueError):
            ParkingTicket(self.parking_ticket.officer, 0)

    def test_report_format(self):
        self.parking_ticket.fine = 25
        report = str(self.parking_ticket)
        self.assertIn("Parking Ticket:", report)
        self.assertIn("Officer: Randall Griggs", report)
        self.assertIn("Badge Number: A2599", report)
        self.assertIn("Car Make: Jeep", report)
        self.assertIn("Car Model: Cherokee", report)
        self.assertIn("Car Color: Black", report)
        self.assertIn("License Number: Honse9", report)
        self.assertIn("Minutes Parked: 120", report)
        self.assertIn("Minutes Purchased: 60", report)
        self.assertIn("Minutes Over: 60", report)
        self.assertIn("Fine: $25", report)
    

if __name__ == "__main__":
    unittest.main()