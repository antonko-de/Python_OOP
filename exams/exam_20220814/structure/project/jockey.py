class Jockey:
    
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
        self.horse = None
        
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, val):
        
        if val.strip() == "":
            raise ValueError("Name should contain at least one character!")
        
        self.__name = val
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, val):
        
        if val < 18:
            raise ValueError("Jockeys must be at least 18 to participate in the race!")
        
        self.__age = val
        
        
    
