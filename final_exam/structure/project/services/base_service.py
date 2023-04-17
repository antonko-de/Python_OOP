from abc import ABC, abstractmethod

class BaseService(ABC):
    
    CAPACITY:int
    
    def __init__(self, name:str) -> None:
        self.name = name
        self.capacity = self.CAPACITY
        self.robots:list = []
        
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, val:str) -> None:
        if val.strip() == '':
            raise ValueError("Service name cannot be empty!")
        
        self.__name = val
        
    @property
    def capacity(self) -> int:
        return self.__capacity
    
    @capacity.setter
    def capacity(self, val:int) -> None:
        if val <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        
        self.__capacity = val
        
    
    @abstractmethod
    def details(self) -> str:
        pass