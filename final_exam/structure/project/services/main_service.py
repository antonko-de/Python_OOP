from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30
    
    def __init__(self, name:str) -> None:
        super().__init__(name)
        
    def details(self) -> str:
        
        if len(self.robots) == 0:
            return f"{self.name} Main Service:\nRobots: none"
        
        return f"{self.name} Main Service:\nRobots: {' '.join([r.name for r in self.robots])}"
