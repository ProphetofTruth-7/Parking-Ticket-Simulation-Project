"The ParkingTicket class represents a infraction ticket a police officer issues to deliquent vehicles. It is called/created when a PoliceOfficer finds an expired parking meter, and handles the calculation of fines and report collating"
class ParkingTicket:
    def __init__(self, officer, fine):
        minute_over = officer.car.minutes_parked - officer.meter.purchased_parking
        if minute_over <= 0:
            raise ValueError("Cannot create a Parking Ticket for a car that is not over the purchased parking time")
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
        minutes_over = self.officer.car.minutes_parked - self.officer.meter.purchased_parking

        if minutes_over <= 0:
            return 0

        fine = 25
        additional = (minutes_over - 1) // 60
        
        return fine + (additional*10)

    "A method that designs how the ParkingTicket object is displayed when printed/returned. This is the collated report with all relevant details"
    def __str__(self): 
        return f"Parking Ticket:\n\nOfficer: {self.officer.name}\nBadge Number: {self.officer.badge_number}\nCar Make: {self.officer.car.make}\nCar Model: {self.officer.car.model}\nCar Color: {self.officer.car.color}\nLicense Number: {self.officer.car.license_number}\nMinutes Parked: {self.officer.car.minutes_parked}\nMinutes Purchased: {self.officer.meter.purchased_parking}\nMinutes Over: {self.officer.car.minutes_parked - self.officer.meter.purchased_parking}\nFine: ${self.fine}\n"