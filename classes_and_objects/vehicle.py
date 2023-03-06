'''Create a class called Vehicle. Upon initialization, it should receive max_speed (integer, optional; 150 by default) and mileage (number).
Create an instance variable called gadgets - an empty list by default.'''

class Vehicle:
    def __init__(self, mileage,max_speed = 150) -> None:
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []