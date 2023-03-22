'''Create an abstract class called Vehicle that should have abstract methods drive and refuel.
Create 2 vehicles that inherit the Vehicle class (a Car and a Truck) and simulates driving and refueling them. Car and Truck both receive fuel_quantity and fuel_consumption in liters per km upon initialization. They both can be driven a given distance: drive(distance) and refueled with a given amount of fuel: refuel(fuel). It is summer, so both vehicles use air conditioners, and their fuel consumption per km when driving is increased by 0.9 liters for the car and 1.6 liters for the truck. Also, the Truck has a tiny hole in its tank, and when it is refueled, it keeps only 95% of the given fuel. The car has no problems and adds all the given fuel to its tank. If a vehicle cannot travel the given distance, its fuel does not change.
Note: Submit all your classes and imports in the judge system
'''

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    
    def __init__(self, fuel_quantity:int, fuel_consumption:int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        
    @abstractmethod
    def drive(self):
        pass
    
    @abstractmethod
    def refuel(self):
        pass
    

class Car(Vehicle):
    
    CONDITIONER_ON = 0.9
    
    def __init__(self, fuel_quantity, fuel_consumption) -> None:
        super().__init__( fuel_quantity, fuel_consumption)
        
    def drive(self, distance):
        if  self.fuel_quantity >= (self.fuel_consumption + Car.CONDITIONER_ON) * distance:
            self.fuel_quantity -= (self.fuel_consumption + Car.CONDITIONER_ON) * distance
    
    def refuel(self, fuel: int):
        self.fuel_quantity += fuel
        
        
class Truck(Vehicle):
    
    CONDITIONER_ON = 1.6
    
    def __init__(self, fuel_quantity, fuel_consumption) -> None:
        super().__init__( fuel_quantity, fuel_consumption)
        
    def drive(self, distance):
        if  self.fuel_quantity >= (self.fuel_consumption + Truck.CONDITIONER_ON) * distance:
            self.fuel_quantity -= (self.fuel_consumption + Truck.CONDITIONER_ON) * distance
    
    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

        
    
    

        