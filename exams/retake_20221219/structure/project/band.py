class Band:
    
    def __init__(self, name:str) -> None:
        self.name = name
        self.members:list = []
        
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, val:str) -> None:
        if val.strip() == "":
            raise ValueError("Band name should contain at least one character!")
        
        self.__name = val
        
        
    def __str__(self) -> str:
        return f"{self.name} with {len(self.members)} members."