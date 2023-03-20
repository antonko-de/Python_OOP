'''The MovieWorld class should receive one parameter upon initialization: name: str. Each MovieWorld instance should also have 2 more attributes:
customers (empty list of Customer objects), dvds (empty list of DVD objects). The class should also have the following methods:
•	dvd_capacity() - returns 15 - the DVD capacity of a movie world
•	customer_capacity() - returns 10 - the customer capacity of a movie world
•	add_customer(customer: Customer) - add the customer if capacity not exceeded
•	add_dvd(dvd: DVD) - add the DVD if capacity not exceeded
•	rent_dvd(customer_id: int, dvd_id: int)
o	If the customer has already rented that DVD return "{customer_name} has already rented {dvd_name}"
o	If the DVD is rented by someone else, return "DVD is already rented"
o	If the customer is not allowed to rent the DVD, return "{customer_name} should be at least {dvd_age_restriction} to rent this movie"
o	Otherwise, the rent is successful (the DVD is rented and added to the customer's DVDs). Return "{customer_name} has successfully rented {dvd_name}"
•	return_dvd(customer_id, dvd_id) - if the DVD is in the customer, he/she should return it and the method should return the message 
"{customer_name} has successfully returned {dvd_name}". Otherwise, return "{customer_name} does not have that DVD" 
•	__repr__() - return the string representation of each customer and each DVD on separate lines
'''

from project.customer import Customer
from project.dvd import DVD

class MovieWorld:
    
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10
    
    def __init__(self, name:str) -> None:
        
        self.name = name
        self.customers:list = []
        self.dvds:list = []
    
    @staticmethod    
    def dvd_capacity() -> int:
        return MovieWorld.DVD_CAPACITY
    
    @staticmethod
    def customer_capacity() -> int:
        return MovieWorld.CUSTOMER_CAPACITY
    
    def add_customer(self, customer:Customer) -> None:
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)
            
    def add_dvd(self, dvd:DVD) -> None:
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)
            
    def rent_dvd(self, customer_id:int, dvd_id:int) -> str:
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        
        if dvd in customer.rented_dvds:
            return  f"{customer.name} has already rented {dvd.name}"
        
        if dvd.is_rented:
            return "DVD is already rented"
        
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        
        
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"
    
    def return_dvd(self, customer_id:int, dvd_id:int) -> str:
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        
        return f"{customer.name} does not have that DVD"
    
    def __repr__(self) -> str:
        
        output = [str(c) for c in self.customers]
        output.extend(str(d) for d in self.dvds)
        
        return "\n".join(output)
         
