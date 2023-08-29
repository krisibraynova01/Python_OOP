from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        ...

    @abstractmethod
    def refuel(self, fuel):
        ...


class Car(Vehicle):
    AIR_CONSUMPTION = 0.9

    def drive(self, distance):
        total_consumption = (self.fuel_consumption + Car.AIR_CONSUMPTION) * distance
        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONSUMPTION = 1.6

    def drive(self, distance):
        total_consumption = (self.fuel_consumption + Truck.AIR_CONSUMPTION) * distance
        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95




