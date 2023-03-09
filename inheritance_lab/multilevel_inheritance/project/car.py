from project.vehicle import Vehicle

class Car(Vehicle):
    
    def __init__(self) -> None:
        super().__init__()
        
    def drive(self):
        return 'driving...'