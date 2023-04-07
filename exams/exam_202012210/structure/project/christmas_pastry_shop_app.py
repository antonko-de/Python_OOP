from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth

class ChristmasPastryShopApp():
    
    VALID_DELICACIES = ["Gingerbread", "Stolen"]
    VALID_BOOTHS = ["Open Booth", "Private Booth"]
    
    def __init__(self) -> None:
        self.booths:list = []
        self.delicacies:list = []
        self.income:float = 0.0
        
    def add_delicacy(self, type_delicacy:str, name:str, price:float):
        
        if name in [d.name for d in self.delicacies]:
            raise Exception(f"{name} already exists!")
        
        if type_delicacy not in ChristmasPastryShopApp.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        
        if type_delicacy == "Gingerbread":
            delicacy = Gingerbread(name, price)
        else:
            delicacy = Stolen(name, price)
            
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth:str, booth_number:int, capacity:int):
        
        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")
        
        if type_booth not in ChristmasPastryShopApp.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")
        
        if type_booth == "Open Booth":
            booth = OpenBooth(booth_number, capacity)
        else:
            booth = PrivateBooth(booth_number, capacity)
            
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."
    
    def reserve_booth(self, number_of_people:int):
        
        try:
            booth = [b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people][0]
        except:
            raise Exception(f"No available booth for {number_of_people} people!")
        
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
    
    
    def order_delicacy(self, booth_number:int, delicacy_name:str):
        
        if not booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Could not find booth {booth_number}!")
        
        if not delicacy_name in [d.name for d in self.delicacies]:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        delicacy = [d for d in self.delicacies if d.name == delicacy_name][0]
        
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."
    
    
    def leave_booth(self, booth_number:int):
        
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        
        bill = booth.price_for_reservation
        bill += sum([d.price for d in booth.delicacy_orders])
        self.income += bill
        
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0
        
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."
    
    def get_income(self):
        return f"Income: {self.income:.2f}lv."


shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.reserve_booth(30))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.get_income())
