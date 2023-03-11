'''Create a class called Topping. Upon initialization, it should receive:
•	topping_type: str - if the topping is an empty string, raise a ValueError with the message "The topping type cannot be an empty string"
•	weight: float - if the weight is 0 or less, raise a ValueError with the message "The weight cannot be less or equal to zero"

'''


class Topping():
    def __init__(self, topping_type:str, weight:float) -> None:
        self.topping_type = topping_type
        self.weight = weight
        
    
    @property
    def topping_type(self):
        return self.__topping_type
    
    @topping_type.setter
    def topping_type(self,  val:str):
        if val == '':
            raise ValueError("The topping type cannot be an empty string")

        self.__topping_type = val
        
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, val):
        if val <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        
        self.__weight = val
        
        