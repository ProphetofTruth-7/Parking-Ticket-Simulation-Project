"The ParkingMeter class represents a parking meter, tracking the amount of time a driver purchased for parking. It is solely used to compare purchased vs used parking time, and specifically utilized by the PoliceOfficer class to check/write parking tickets"
class ParkingMeter:
    def __init__(self, purchased_parking):
        self.purchased_parking = purchased_parking

    "Mandatory getter property for the ParkingMeter class' variable purchased_parking"
    @property
    def purchased_parking(self):
        return self._purchased_parking

    "Mandatory setter property for the ParkingMeter class' variable purchased_parking"
    @purchased_parking.setter
    def purchased_parking(self,value):
        if not value >= 0:
            raise ValueError("Minutes Purchased must be greater than or equal to 0")
        if not isinstance(value, int):
            raise ValueError("Minutes Purchased must be an Integer")
        self._purchased_parking = value
