'''The Animal class is a base class for any type of animal in the zoo. It should receive four public attributes - a name (string),
a gender (str), an age (int), and a money_for_care (int) upon initialization.
The Animal class should also have 1 additional method:
· __repr__() - returns string representation of the animal in the format: "Name: {name}, Age: {age}, Gender: {gender}"'''

class Animal:
    
    def __init__(self, name: str, gender:str, age:int, money_for_care:int) -> None:
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care
        
    def __repr__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"