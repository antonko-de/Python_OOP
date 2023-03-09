from project.animal import Animal


class Cat(Animal):
    
    def __init__(self) -> None:
        super().__init__()
        
    
    def meow(self):
        return "meowing..."