from parking_meter import ParkingMeter
from police_officer import PoliceOfficer
from parked_car import ParkedCar

car = ParkedCar("Toyota", "Camry", "Blue", "RARBRED", 120)
meter = ParkingMeter(60)
officer = PoliceOfficer("Alfram Jericho", "34-004-561", car, meter)


officer.issue_ticket()