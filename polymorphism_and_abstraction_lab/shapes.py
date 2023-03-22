'''Create an abstract class Shape with abstract methods calculate_area and calculate_perimeter. 
Create classes Circle (receives radius upon initialization) and Rectangle (receives height and width upon initialization) that implement those methods (returning the result). The fields of Circle and Rectangle should be private.
Submit all the classes and your imports in the judge system
'''

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass
    

class Circle(Shape):
    
    def __init__(self, radius) -> None:
        self.__radius = radius
        
    def calculate_area(self):
        return pi * self.__radius **  2
    
    def calculate_perimeter(self):
        return 2 * pi * self.__radius
    

class Rectangle(Shape):
    
    def __init__(self, height, width) -> None:
        self.__height = height
        self.__width = width
        
    def calculate_area(self):
        return self.__height * self.__width
    
    def calculate_perimeter(self):
        return 2 * self.__height  + 2 * self.__width
    