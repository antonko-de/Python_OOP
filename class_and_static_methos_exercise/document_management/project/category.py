'''The Category class should receive the following parameters upon initialization: id: int, name: str. The class should have two methods:
•	edit(new_name: str) - edit the name of the category
•	__repr__() - returns a string representation of the category in the following format: "Category {id}: {name}"
'''

class Category:
    
    def __init__(self, id:int, name:str, ) -> None:
        self.id = id
        self.name = name
        
    def edit(self,new_name:str) -> None:
        self.name = new_name
        
    def __repr__(self) -> str:
        return f"Category {self.id}: {self.name}" 
        
        