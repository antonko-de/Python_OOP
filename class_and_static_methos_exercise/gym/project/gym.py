'''Upon initialization, the class will not receive any parameters. However, it should have the following attributes: customers (empty  list of customer objects), 
trainers (empty list of trainer objects), equipment (empty list of equipment objects), plans (empty list of plan objects), subscriptions (empty list of subscription objects)
Create the following methods:
•	add_customer(customer: Customer) - add the customer in the customer list if the customer is not already in it
•	add_trainer(trainer: Trainer) - add the trainer to the trainers' list, if the trainer is not already in it
•	add_equipment(equipment: Equipment) - add the equipment to the equipment list, if the equipment is not already in it
•	add_plan(plan: ExercisePlan) - add the plan to the plans' list, if the plan is not already in it
•	add_subscription(subscription: Subscription) - add the subscription in the subscriptions list if the subscription is not already in it
•	subscription_info(subscription_id: int) - get the subscription, the customer, the trainer, the equipment, and the plan. Then return their string representations each on a new line.
'''

from project.subscription import Subscription
from project.exercise_plan import ExercisePlan
from project.equipment import Equipment
from project.trainer import Trainer
from project.customer import Customer


class Gym:
    
    def __init__(self) -> None:
        self.customers:list = []
        self.trainers:list = []
        self.equipment:list = []
        self.plans:list = []
        self.subscriptions:list = []
    
    @staticmethod
    def find_add_object(obj, collection:list,):
        if obj not in collection:
            collection.append(obj)
            
    def add_customer(self, customer:Customer):
        Gym.find_add_object(customer, self.customers)
        
    def add_trainer(self, trainer:Trainer):
        Gym.find_add_object(trainer, self.trainers)
        
    def add_equipment(self, equipment:Equipment):
        Gym.find_add_object(equipment, self.equipment)
        
    def add_plan(self, plan:ExercisePlan):
        Gym.find_add_object(plan, self.plans)
        
    def add_subscription(self,subscription:Subscription):
        Gym.find_add_object(subscription, self.subscriptions)
    
    def subscription_info(self, subcription_id:int) ->str:
        
        def get_info(val, attr:str, collection):
            for obj in collection:
                if getattr(obj, attr) == val:
                    return obj
                
        output = []
        subscription = get_info(val=subcription_id, attr="id", collection=self.subscriptions)
        output.append(str(subscription))
        customer = get_info(val=subscription.customer_id, attr='id', collection=self.customers)
        output.append(str(customer))
        trainer = get_info(val=subscription.trainer_id, attr='id', collection=self.trainers)
        output.append(str(trainer))
        plan = get_info(val=subscription.exercise_id, attr="id", collection=self.plans)
        equipment = get_info(val=plan.equipment_id, attr='id', collection=self.equipment)
        output.append(str(equipment))
        output.append(str(plan))
        
        return '\n'.join(output)
        
        
                
        