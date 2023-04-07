from project.horse_specification.horse import Horse

class Thoroughbred(Horse):
    MAXIMUM_SPEED = 140
    
    def __init__(self, name:str, speed:int) -> None:
        super().__init__(name, speed)
        
    def train(self):
        if self.speed + 3 > Thoroughbred.MAXIMUM_SPEED:
            self.speed = Thoroughbred.MAXIMUM_SPEED
        else:
            self.speed += 3
            
            

