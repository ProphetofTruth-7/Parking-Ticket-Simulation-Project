from parking_ticket import ParkingTicket
from parked_car import ParkedCar
from parking_meter import ParkingMeter

class PoliceOfficer:
    def __init__(self, name, badge_number, car: "ParkedCar", meter: "ParkingMeter"):
        self.name = name
        self.badge_number = badge_number
        self.car = car
        self.meter = meter

    @property
    def name(self):
        return self._name
    @property
    def badge_number(self):
        return self._badge_number

    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @badge_number.setter
    def badge_number(self,value):
        if not isinstance(value, str):
            raise ValueError("Badge Number must be a string")
        self._badge_number = value

    def issue_ticket(self):
        if self.car.minutes_parked > self.meter.purchased_parking:
            ticket = ParkingTicket(self, 0)
            ticket._fine = ticket.calculate_fine()
            return ticket
        else:
            print (f"AMONGUS")
            return None