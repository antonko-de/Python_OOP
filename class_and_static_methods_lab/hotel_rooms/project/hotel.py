from project.room import Room

class Hotel:
    def __init__(self, name:str) -> None:
        self.name = name
        self.rooms = []
        self.guests  = 0
        
    @classmethod
    def from_stars(cls, stars_count:int):
        return cls(f"{stars_count} stars Hotel")
            
    def add_room(self, room:Room)->None:
        self.rooms.append(room)
    
    def take_room(self, room_number:int, people:int)->None:
        room = [r for r in self.rooms if r.number == room_number][0]
        room.take_room(people)
        if room.is_taken:
            self.guests += people
            
    def free_room(self, room_number:int)->None:
        room = [r for r in self.rooms if r.number == room_number][0]
        guests = room.guests
        room.free_room()
        if not room.is_taken:
            self.guests -= guests
            
    def status(self):
        return f"""Hotel {self.name} has {self.guests} total guests
Free rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}
Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}"""

        



    
        
        
             