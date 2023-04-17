from abc import ABC, abstractmethod

class BaseRobot(ABC):
    
    INITIAL_WEIGHT:int
    
    def __init__(self, name:str, kind:str, price:float ) -> None:
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = self.INITIAL_WEIGHT
        
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, val:str) -> None:
       if val.strip() == '':
           raise ValueError("Robot name cannot be empty!")
       
       self.__name = val
    
    @property
    def kind(self) -> str:
        return self.__kind
    
    @kind.setter
    def kind(self, val:str) -> None:
       if val.strip() == '':
           raise ValueError("Robot kind cannot be empty!")
       
       self.__kind = val
        
    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, val:float) -> None:
       if val <= 0.0:
           raise ValueError("Robot price cannot be less than or equal to 0.0!")
       
       self.__price = val
       
    @abstractmethod
    def eating(self) -> None:
        pass