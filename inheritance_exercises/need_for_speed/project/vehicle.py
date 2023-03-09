class Vehicle:
    
    DEFAULT_FUEL_CONSUMPTION:float = 1.25
    
    def __init__(self, fuel:float, horse_power:int) -> None:
        
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power
        
    def drive(self, kilometers:int):
        
        if kilometers * self.fuel_consumption <= self.fuel:
            self.fuel -= kilometers * self.fuel_consumption
            
            

        