'''The Zoo class should receive 4 attributes upon initialization:
•	Public attribute name: string
•	Private attribute budget: int
•	Private attribute animal_capacity: int
•	Private attribute workers_capacity: int
It should also have 2 instance attributes:
•	Public attribute animals: list - (empty upon initialization)
•	Public attribute workers: list - (empty upon initialization)
The Zoo class should also have 8 methods:
•	add_animal(animal, price)
o	If you have enough budget and capacity add the animal (instance of Lion/Tiger/Cheetah) to the animals' list, 
reduce the budget, and return "{name} the {type of animal (Lion/Tiger/Cheetah)} added to the zoo"
o	If you have the capacity, but no budget, return "Not enough budget"
o	In any other case, you do not have space, and you should return "Not enough space for animal"
•	hire_worker(worker)
o	If you have not exceeded the capacity of workers in the zoo for the worker (instance of Keeper/Caretaker/Vet), 
add him to the workers and return "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"
o	Otherwise, return "Not enough space for worker"
•	fire_worker(worker_name)
o	If there is a worker with that name in the workers' list, remove him and return "{worker_name} fired successfully"
o	Otherwise, return "There is no {worker_name} in the zoo"
•	pay_workers()
o	If you have enough budget to pay the workers (sum their salaries) pay them and return "You payed your workers. They are happy. Budget left: {left_budget}"
o	Otherwise, return "You have no budget to pay your workers. They are unhappy"
•	tend_animals()
o	If you have enough budget to take care of the animals, reduce the budget and return "You tended all the animals. They are happy. Budget left: {left_budget}"
o	Otherwise, return "You have no budget to tend the animals. They are unhappy."
•	profit(amount)
o	Increase the budget with the given amount of profit
•	animals_status()
'''
from project.worker import Worker
from project.animal import Animal



class Zoo:
    
    def __init__(self, name:str, budget:int, animal_capacity:int, workers_capacity:int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals:list = []
        self.workers:list = []
        
    def add_animal(self, animal:Animal, price)->str:
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        
        if self.__budget < price:
            return "Not enough budget"
        
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
    
    def hire_worker(self, worker:Worker):
        if self.__workers_capacity <= len(self.workers):
            return f"Not enough space for worker"
        
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"
    
    def fire_worker(self, worker_name:str) -> str:
        try:
            fired = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"
        
        self.workers.remove(fired)
        return f"{worker_name} fired successfully"
    
    def pay_workers(self) -> None:
        total_salaries = 0
        
        for worker in self.workers:
            total_salaries += worker.salary
            
        if total_salaries > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"
        
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"
    
    def tend_animals(self) -> None:
        total_cost = 0
        
        for animal in self.animals:
            total_cost += animal.money_for_care
            
        if total_cost > self.__budget:
            return f"You have no budget to tend the animals. They are unhappy."
        
        self.__budget -= total_cost
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
    
    def profit(self, amount:int) -> None:
        self.__budget += amount
        
    
    def __type_dict(self, list_of_objects) -> dict:
        parsed_dict = {}
        
        for item in list_of_objects:
            if not item.__class__.__name__  + 's'in parsed_dict.keys():
                parsed_dict[item.__class__.__name__ + 's'] = []
                parsed_dict[item.__class__.__name__ + 's'].append(item)
            else:
                parsed_dict[item.__class__.__name__+ 's'].append(item)
                
        return parsed_dict
    
    def animals_status(self):
        dict_animals = self.__type_dict(self.animals)
        output = []
        output.append(f"You have {len(self.animals)} animals")
        
        for animal_type in ["Lions", "Tigers", "Cheetahs"]:
            output.append(f"----- {len(dict_animals[animal_type])} {animal_type}:")
            output.extend(dict_animals[animal_type])
            
        return '\n'.join([str(i) for i in output])
        
    def workers_status(self):
        dict_workers = self.__type_dict(self.workers)
        output = []
        output.append(f"You have {len(self.workers)} workers")
        
        for worker_type in ["Keepers", "Caretakers", "Vets" ]:
            output.append(f"----- {len(dict_workers[worker_type])} {worker_type}:")
            output.extend(dict_workers[worker_type])
    
        return '\n'.join([str(i) for i in output])
        
            
        
        
        
    
            
        
        
            
        
        
    
            
            
            
    