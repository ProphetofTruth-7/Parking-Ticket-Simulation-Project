import unittest
from unittest.mock import Mock
from police_officer import PoliceOfficer


class TestPoliceOfficer(unittest.TestCase):
    def setUp(self):
        car = Mock(make="Chevy", model="Mailbu", color="Champagne", license_number="MONGUS", minutes_parked=120)
        meter = Mock(purchased_parking=60)
        self.police_officer = PoliceOfficer("Count Frollo", "HELLFIRE666", car, meter)

    def test_exact_invalid_ticket(self):
        self.police_officer.car.minutes_parked = 60
        ticket = self.police_officer.issue_ticket()
        self.assertIsNone(ticket)
    def test_lesser_invalid_ticket(self):
        self.police_officer.car.minutes_parked = 30
        ticket = self.police_officer.issue_ticket()
        self.assertIsNone(ticket)
    def test_valid_ticket(self):
        self.police_officer.car.minutes_parked = 61
        ticket = self.police_officer.issue_ticket()
        self.assertIsNotNone(ticket)

    def test_correct_officer_info(self):
        ticket = self.police_officer.issue_ticket()
        self.assertEqual(ticket.officer.name, "Count Frollo")
        self.assertEqual(ticket.officer.badge_number, "HELLFIRE666")

    def test_correct_car_info(self):
        ticket = self.police_officer.issue_ticket()
        self.assertEqual(ticket.officer.car.make, "Chevy")
        self.assertEqual(ticket.officer.car.model, "Mailbu")
        self.assertEqual(ticket.officer.car.color, "Champagne")
        self.assertEqual(ticket.officer.car.license_number, "MONGUS")

if __name__ == "__main__":
    unittest.main()
