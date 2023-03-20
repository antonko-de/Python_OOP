'''Upon initialization, the DVD class should receive the following parameters: name: str, id: int, creation_year: int, 
creation_month: str, age_restriction: int. Each DVD should also have an attribute called is_rented (False by default)
Create a method called from_date(id: int, name: str, date: str, age_restriction: int) - it should create a new instance using the provided data. 
The date will be in the format "day.month.year" - all of them should be numbers.
Implement the __repr__ method so it returns the following string: "{id}: {name} ({creation_month} {creation_year}) has age restriction 
{age_restriction}. Status: {rented/not rented}"
'''

from calendar import month_name
class DVD:
    
    def __init__(self, name:str, id:int, creation_year:int, creation_month, age_restriction:int) -> None:
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False
        
    @classmethod
    def from_date(cls, id:int, name:str, date:str, age_restriction:int):
        month, year = date.split(".")[1::]
        
        return cls(name=name, id=id, creation_year = int(year), creation_month = month_name[int(month)], age_restriction=age_restriction)
    
    
    def __repr__(self) -> str:
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"
    

