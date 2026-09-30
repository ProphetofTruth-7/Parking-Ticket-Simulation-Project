class ParkingTicket:
    def __init__(self, officer, fine):
        self.officer = officer
        self.fine = fine

    @property
    def fine(self):
        return self._fine

    @fine.setter
    def fine(self,value):
        if not value >= 0:
            raise ValueError("Fine must be greater than or equal to 0")
        if not isinstance(value, int):
            raise ValueError("Fine must be an Integer")
        self._fine = value

    def calculate_fine(self):   #Since the Parking Ticket object even exists, its assumed that we're already over. No validation neccessary
        fine = 25
        minutes_over = self.officer.car.minutes_parked - self.officer.meter.purchased_parking
        if minutes_over > 60:
            additional = 1 + ((minutes_over - 60) // 60)
            fine += (additional * 10)
        return fine

    def __str__(self): 
        return f"Parking Ticket:\n\nOfficer: {self.officer.name}\nBadge Number: {self.officer.badge_number}\nCar Make: {self.officer.car.make}\nCar Model: {self.officer.car.model}\nCar Color: {self.officer.car.color}\nLicense Number: {self.officer.car.license_number}\nMinutes Parked: {self.officer.car.minutes_parked}\nMinutes Purchased: {self.officer.meter.purchased_parking}\nMinutes Over: {self.officer.car.minutes_parked - self.officer.meter.purchased_parking}\nFine: ${self.fine}\n"