from abc import ABC, abstractmethod

class Horse(ABC):
    
    MAXIMUM_SPEED = None
    
    def __init__(self, name:str, speed:int) -> None:
        self.name = name
        self.speed = speed
        self.is_taken = False
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, val):
        if len(val) < 4:
            raise ValueError(f"Horse name {val} is less than 4 symbols!")
        
        self.__name = val
        
        
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, val):
        if self.MAXIMUM_SPEED < val:
            raise ValueError(f"Horse speed is too high!")\
        
        self.__speed = val
        
    @abstractmethod
    def train(self):
        pass
        
    