from abc import ABC, abstractmethod

class Food(ABC):
    
    @abstractmethod
    def __init__(self, quantity:int) -> None:
        self.quantity = quantity