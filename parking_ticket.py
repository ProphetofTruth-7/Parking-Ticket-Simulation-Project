class ParkingTicket:
    def __init__(self, officer, fine):
        self.officer = officer
        self.fine = fine

    @property
    def fine(self):
        return self._fine

    def calculate_fine(self):   #Since the Parking Ticket object even exists, its assumed that we're already over. No validation neccessary
        fine = 25
        minutes_over = self.officer.car.minutes_parked - self.officer.meter.purchased_parking
        if minutes_over > 60:
            additional = (minutes_over - 60) // 60
            fine += (additional * 10)
        return fine