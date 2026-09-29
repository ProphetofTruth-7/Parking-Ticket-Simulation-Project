class PoliceOfficer:
    def __init__(self, name, badge_number, car: ParkedCar, meter: ParkingMeter):
        self.name = name
        self.badge_number = badge_number
        self.car = car
        self.meter = meter