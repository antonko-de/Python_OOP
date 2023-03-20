'''Create a class called Calculator that has the following static methods:
•	add(*args) - sums all the arguments passed to the function and returns the result
•	multiply(*args) - multiplies all the numbers and returns the result
•	divide(*args) - divides all the numbers (starting from the first one) and returns the result
•	subtract(*args) - subtracts all the numbers (starting from the first one) and returns the result
'''
from functools import reduce

class Calculator():
    
    @staticmethod
    def add(*args):
        result =sum(args)
        return result
    
    @staticmethod
    def multiply(*args):
        result = reduce(lambda x, y: x * y, args)
        return result   
    
    @staticmethod
    def divide(*args):
        result = reduce(lambda x, y: x / y, args) 
        return result
    
    @staticmethod
    def subtract(*args):
        result = reduce(lambda x, y: x-y, args)
        return result
    

