from project.horse_specification.horse import Horse

class Appaloosa(Horse):
    MAXIMUM_SPEED = 120
    
    def __init__(self, name:str, speed:int) -> None:
        super().__init__(name, speed)
        
    def train(self):
        if self.speed + 2 > Appaloosa.MAXIMUM_SPEED:
            self.speed = Appaloosa.MAXIMUM_SPEED
        else:
            self.speed += 2
        
        
