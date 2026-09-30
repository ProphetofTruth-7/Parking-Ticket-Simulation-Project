"The ParkingTicket class represents a infraction ticket a police officer issues to deliquent vehicles. It is called/created when a PoliceOfficer finds an expired parking meter, and handles the calculation of fines and report collating"
class ParkingTicket:
    def __init__(self, officer, fine):
        self.officer = officer
        self.fine = fine

    "Mandatory getter property for the ParkingTicket class' variable fine"
    @property
    def fine(self):
        return self._fine

    "Mandatory setter property for the ParkingTicket class' variable fine"
    @fine.setter
    def fine(self,value):
        if not value >= 0:
            raise ValueError("Fine must be greater than or equal to 0")
        if not isinstance(value, int):
            raise ValueError("Fine must be an Integer")
        self._fine = value
    
    "A method that calculates the fine for the ParkingTicket object base don values retrieved from the PoliceOfficer object that created it."
    def calculate_fine(self):   #Since the Parking Ticket object even exists, its assumed that we're already over our purchased time. No validation necessary
        fine = 25
        minutes_over = self.officer.car.minutes_parked - self.officer.meter.purchased_parking
        if minutes_over > 60:
            additional = 1 + ((minutes_over - 60) // 60)
            fine += (additional * 10)
        return fine

    "A method that designs how the ParkingTicket object is displayed when printed/returned. This is the collated report with all relevant details"
    def __str__(self): 
        return f"Parking Ticket:\n\nOfficer: {self.officer.name}\nBadge Number: {self.officer.badge_number}\nCar Make: {self.officer.car.make}\nCar Model: {self.officer.car.model}\nCar Color: {self.officer.car.color}\nLicense Number: {self.officer.car.license_number}\nMinutes Parked: {self.officer.car.minutes_parked}\nMinutes Purchased: {self.officer.meter.purchased_parking}\nMinutes Over: {self.officer.car.minutes_parked - self.officer.meter.purchased_parking}\nFine: ${self.fine}\n"