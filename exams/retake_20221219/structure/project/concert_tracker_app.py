#from project.band_members.musician import Musician
from project.band import Band
from project.band_members.guitarist import Guitarist
from project.band_members.drummer import Drummer
from project.band_members.singer import Singer
from project.concert import Concert

class ConcertTrackerApp:
    
    VALID_MUSICIAN_TYPES = ["Guitarist", "Drummer", "Singer"]
    
    CONCERT_REQUIERMENTS = {"Rock": {'Guitarist': "play rock", 'Drummer': 'play the drums with drumsticks', 'Singer': "sing high pitch notes"},
                            "Metal": {'Guitarist': "play metal", 'Drummer': 'play the drums with drumsticks', 'Singer': "sing low pitch notes"},
                            "Jazz": {'Guitarist': "play jazz", 'Drummer': 'play the drums with drum brushes', 'Singer': ["sing high pitch notes", "sing low pitch notes"]}}
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []
        
    
    def create_musician(self, musician_type:str, name:str, age:int) -> str:
        
        if musician_type not in ConcertTrackerApp.VALID_MUSICIAN_TYPES:
            raise ValueError(f"Invalid musician type!")
        
        if name in [m.name for m in self.musicians]:
            raise Exception(f"{name} is already a musician!")
        
       
        if musician_type == "Guitarist":
            musician = Guitarist(name, age)
        elif musician_type == "Drummer":
            musician = Drummer(name, age)
        else: 
            musician = Singer(name, age)
        
        self.musicians.append(musician)
        return f"{musician.name} is now a {musician.__class__.__name__}."
    
    
    def create_band(self, name:str) -> str:
        
        if name in [b.name for b in self.bands]:
            raise Exception(f"{name} band is already created!")
        
        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."
    
    def create_concert(self, genre:str, audience:int, ticket_price:float, expenses:float, place:str) -> str:
        if place in [c.place for c in self.concerts]:
            raise Exception(f"{place} is already registered for {genre} concert!")
        
        concert = Concert(genre, audience, ticket_price, expenses, place)
        
        self.concerts.append(concert)
        return f"{concert.genre} concert in {concert.place} was added."
    
    def add_musician_to_band(self, musician_name:str, band_name:str) -> str:
        
        if not musician_name in [m.name for m in self.musicians]:
            raise Exception(f"{musician_name} isn't a musician!")
        
        if not band_name in [b.name for b in self.bands]:
            raise Exception(f"{band_name} isn't a band!")
        
        musician = [m for m in self.musicians if m.name == musician_name][0]
        band = [b for b in self.bands if b.name == band_name][0]
        band.members.append(musician)
        return f"{musician.name} was added to {band.name}."
    
    
    def remove_musician_from_band(self, musician_name:str, band_name:str) -> str:
        
        if not band_name in [b.name for b in self.bands]:
            raise Exception(f"{band_name} isn't a band!")
        
        band = [b for b in self.bands if b.name == band_name][0]
        
        if not musician_name in [m.name for m in band.members]:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        
        
        musician = [m for m in self.musicians if m.name == musician_name][0]
        band.members.remove(musician)
        return f"{musician.name} was removed from {band.name}."
    
    def concert_reqierments(self, concert_type: str, drummer:Drummer, singer:Singer, guitarist:Guitarist):
        
        if concert_type == "Rock":

            if (ConcertTrackerApp.CONCERT_REQUIERMENTS["Rock"]["Drummer"] in drummer.skills 
                and ConcertTrackerApp.CONCERT_REQUIERMENTS["Rock"]["Singer"] in singer.skills 
                and ConcertTrackerApp.CONCERT_REQUIERMENTS["Rock"]["Guitarist"] in guitarist.skills):
                return True
            
            else:
                return False
            
        elif concert_type == "Metal":
            
            if (ConcertTrackerApp.CONCERT_REQUIERMENTS["Metal"]["Drummer"] in drummer.skills 
                and ConcertTrackerApp.CONCERT_REQUIERMENTS["Metal"]["Singer"] in singer.skills 
                and ConcertTrackerApp.CONCERT_REQUIERMENTS["Metal"]["Guitarist"] in guitarist.skills):
                return True
            
            else:
                return False
            
        elif concert_type == "Jazz":
            if (ConcertTrackerApp.CONCERT_REQUIERMENTS["Jazz"]["Drummer"] in drummer.skills 
                and ConcertTrackerApp.CONCERT_REQUIERMENTS["Jazz"]["Singer"][0] in singer.skills 
                and ConcertTrackerApp.CONCERT_REQUIERMENTS["Jazz"]["Singer"][1] in singer.skills 
                and ConcertTrackerApp.CONCERT_REQUIERMENTS["Jazz"]["Guitarist"] in guitarist.skills):
                return True
            
            else:
                return False
            
    
    def start_concert(self, concert_place:str, band_name:str) -> str:
        
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]
        
        if set(m.__class__.__name__ for m in band.members) != set(ConcertTrackerApp.VALID_MUSICIAN_TYPES):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        
        drummer = [m for m in band.members if m.__class__.__name__ == "Drummer"][0]
        singer = [m for m in band.members if m.__class__.__name__ == "Singer"][0]
        guitarist = [m for m in band.members if m.__class__.__name__ == "Guitarist"][0]
        
        if not self.concert_reqierments(concert.genre, drummer, singer, guitarist):
            raise Exception (f"The {band.name} band is not ready to play at the concert!")
        
        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
        
          