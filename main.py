from parking_meter import ParkingMeter
from police_officer import PoliceOfficer
from parked_car import ParkedCar

car = ParkedCar("Toyota", "Camry", "Blue", "RARBRED", 121)
meter = ParkingMeter(60)
officer = PoliceOfficer("Alfram Jericho", "A34-004-561", car, meter)


ticket = officer.issue_ticket()
if ticket is not None:
    print(ticket)