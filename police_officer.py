"The PoliceOfficer class represents a police officer who can issue parking tickets. It is the main driver of this program, taking note of the parking_car and parking_meter objects and creating a parking_ticket object if an issue arises"
class PoliceOfficer:
    def __init__(self, name, badge_number, car, meter):
        self.name = name
        self.badge_number = badge_number
        self.car = car
        self.meter = meter

    "Mandatory getter property for the PoliceOfficer class' variable name"
    @property
    def name(self):
        return self._name
    "Mandatory getter property for the PoliceOfficer class' variable badge_number"
    @property
    def badge_number(self):
        return self._badge_number

    "Mandatory setter property for the PoliceOfficer class' variable name"
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value
    "Mandatory setter property for the PoliceOfficer class' variable name"
    @badge_number.setter
    def badge_number(self,value):
        if not isinstance(value, str):
            raise ValueError("Badge Number must be a string")
        self._badge_number = value

    "The issue_ticket function checks if the parked car has exceeded the purchased parking time. If it has, it creates a parking ticket object and calculates the fine, before returning the ticket for printing"
    def issue_ticket(self):
        from parking_ticket import ParkingTicket

        if self.car.minutes_parked > self.meter.purchased_parking:
            ticket = ParkingTicket(self, 0)
            ticket.fine = ticket.calculate_fine()
            return ticket
        else:
            return None