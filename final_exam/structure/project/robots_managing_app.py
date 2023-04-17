from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService

class RobotsManagingApp():
    
    VALID_TYPES_SERVICES = ["MainService", "SecondaryService"]
    VALID_TYPES_ROBOTS = ["MaleRobot", "FemaleRobot"]
    SERVICE_DEPENDENCY = {'MaleRobot': 'MainService', 'FemaleRobot': 'SecondaryService'}
    
    def __init__(self) -> None:
        
        self.robots:list = []
        self.services:list = []
        
    def add_service(self, service_type:str, name:str) -> str:
        #check valid service and if yes create and add it to the list
        if service_type not in RobotsManagingApp.VALID_TYPES_SERVICES:
            raise Exception("Invalid service type!")

        if service_type == "MainService":
            self.services.append(MainService(name))
        elif service_type == "SecondaryService":
            self.services.append(SecondaryService(name))
            
        return f"{service_type} is successfully added."
    
    def add_robot(self, robot_type:str, name:str, kind:str, price:float):
        # check valid robot and if yes create and add it to the list 
        if robot_type not in RobotsManagingApp.VALID_TYPES_ROBOTS:
            raise Exception("Invalid robot type!")
        
        if robot_type == "MaleRobot":
            self.robots.append(MaleRobot(name, kind, price))
        elif robot_type == "FemaleRobot":
            self.robots.append(FemaleRobot(name, kind, price))
        
        return f"{robot_type} is successfully added."
    
    def add_robot_to_service(self, robot_name:str, service_name:str):
        # check if robot depency is correct, check if enough capacity and if yes add the robot
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]
        if not service.__class__.__name__ == RobotsManagingApp.SERVICE_DEPENDENCY[robot.__class__.__name__]:
            return f"Unsuitable service."
        
        
        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")
        
        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."
    
    def remove_robot_from_service(self,  robot_name:str, service_name:str):
        # check if robot is in service and if yes remove it
        service = [s for s in self.services if s.name == service_name][0]
        
        try:
            robot = [r for r in service.robots if r.name == robot_name][0]
            
        except IndexError:
            raise Exception("No such robot in this service!")
        
        service.robots.remove(robot)
        self.robots.append(robot)
        
        return f"Successfully removed {robot_name} from {service_name}."
    
    def feed_all_robots_from_service(self, service_name:str):
    
        service = [s for s in self.services if s.name == service_name][0]
        
        for robot in service.robots:
            robot.eating()
            
        return f"Robots fed: {len(service.robots)}."
    
    def service_price(self, service_name:str):
        # check if service is in the list and if yes return the price
        service = [s for s in self.services if s.name == service_name][0]
        total_price = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."
       
    
    def __str__(self) -> str:
        output = ''
        output +='\n'.join([s.details() for s in self.services])
        return output




