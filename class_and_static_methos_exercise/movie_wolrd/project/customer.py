'''Upon initialization, the Customer class should receive the following parameters: name: str, age: int, id: int.
    Each customer should also have an instance attribute called rented_dvds (empty list with DVD instances).
Implement the __repr__ method, so it returns the following string: "{id}: {name} of age {age} has 
{count_rented_dvds} rented DVD's ({dvd_names joined by comma and space})"
'''

class Customer:
    
    def __init__(self, name:str, age:int, id:int) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds:list = []
        
    def __repr__(self) -> str:
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join(d.name for d in self.rented_dvds)})"