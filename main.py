from parking_meter import ParkingMeter
from police_officer import PoliceOfficer
from parked_car import ParkedCar

car = ParkedCar("Toyota", "Camry", "Blue", "RARBRED", 120)
meter = ParkingMeter(60)
officer = PoliceOfficer("Alfram Jericho", "A34311", car, meter)