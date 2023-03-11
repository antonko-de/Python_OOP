'''Create a class called Dough. Upon initialization, it should receive:
•	flour_type_type: str - if the flour_type type is an empty string, raise a ValueError with the message "The flour_type type cannot be an empty string"
•	baking_technique: str - if the technique is an empty string, raise a ValueError with the message "The baking technique cannot be an empty string"
•	weight: float - if the weight is 0 or less, raise a ValueError with the message "The weight cannot be less or equal to zero"
'''

class Dough():
    def __init__(self, flour_type:str, baking_technique:str, weight:float) -> None:
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight
        
    @property
    def flour_type(self)->str:
        return self.__flour_type
    
    @flour_type.setter
    def flour_type(self, val)-> None:
        if val == '':
            raise ValueError("The flour type cannot be an empty string")
        
        self.__flour_type = val
    
    @property
    def baking_technique(self)->str:
        return self.__baking_technique 
    
    @baking_technique.setter
    def baking_technique(self, val)->None:
        if val == '':
            raise ValueError("The baking technique cannot be an empty string")
        
        self.__baking_technique = val
        
    @property
    def weight(self)->float:
        return self.__weight
    
    @weight.setter
    def weight(self, val)-> None:
        if val <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        
        self.__weight = val
        
    