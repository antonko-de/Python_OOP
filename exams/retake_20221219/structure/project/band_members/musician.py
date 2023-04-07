from abc import ABC, abstractmethod

class Musician(ABC):
    
    ALLOWED_SKILLS = []
    
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
        self.skills = []
        
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, val:str) -> None:
        if val.strip() == "":
            raise ValueError("Musician name cannot be empty!")

        self.__name = val
        
    @property
    def age(self) -> int:
        return self.__age
    
    @age.setter
    def age(self, val:int) -> None:
        if val < 16:
            raise ValueError("Musicians should be at least 16 years old!")
        
        self.__age = val
    
    @abstractmethod
    def learn_new_skill(self, new_skill:str):
        pass
        
    
        