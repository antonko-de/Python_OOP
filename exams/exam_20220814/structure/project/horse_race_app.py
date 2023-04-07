from project.horse_specification.thoroughbred import Thoroughbred
from project.horse_specification.appaloosa import Appaloosa
from project.jockey import Jockey
from project.horse_race import HorseRace

class HorseRaceApp:
    
    VALID_HORSE_TYPES = ["Thoroughbred", "Appaloosa"]
    
    def __init__(self) -> None:
        
        self.horses = []
        self.jockeys = []
        self.horse_races = []
        
    
    def add_horse(self, horse_type:str, horse_name:str, horse_speed:int):
        
        if horse_type in HorseRaceApp.VALID_HORSE_TYPES:
            
            if horse_name in [h.name for h in self.horses]:
                raise Exception(f"Horse {horse_name} has been already added!")
            
            if horse_type == "Thoroughbred":
                horse = Thoroughbred(horse_name, horse_speed)
            else:
                horse = Appaloosa(horse_name, horse_speed)
            
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."
        
        return
        
    
    def add_jockey(self, jockey_name:str, age:int):
        
        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."
    
    def create_horse_race(self, race_type):
        if race_type in [h.race_type for h in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")
        
        horse_race = HorseRace(race_type)
        self.horse_races.append(horse_race)
        return f"Race {race_type} is created."
    
    def add_horse_to_jockey(self, jockey_name:str, horse_type:str):
            
            if jockey_name not in [j.name for j in self.jockeys]:
                raise Exception(f"Jockey {jockey_name} could not be found!")
            
            #check if we have a horse that is not_taken and is of the given type
            try:
                horse = [h for h in self.horses if h.__class__.__name__ == horse_type and not h.is_taken][-1]
            except Exception:
                raise Exception(f"Horse breed {horse_type} could not be found!")
            
            jockey = [j for j in self.jockeys if j.name == jockey_name][0]
            
            if not jockey.horse == None:
                return (f"Jockey {jockey_name} already has a horse.")
            
            horse.is_taken = True
            jockey.horse = horse
            return f"Jockey {jockey_name} will ride the horse {horse.name}."


    def add_jockey_to_horse_race(self, race_type:str, jockey_name:str):
        try:
            horse_race = [r for r in self.horse_races if r.race_type == race_type][0]
        except Exception:
            raise Exception(f"Race {race_type} could not be found!")
        
        try:
            jockey = [j for j in self.jockeys if j.name == jockey_name][0]
        except Exception:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        
        if jockey.horse == None:
             raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
         
        if jockey in horse_race.jockeys:
            return(f"Jockey {jockey_name} has been already added to the {race_type} race.")
        
        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."
    
    def start_horse_race(self,race_type:str):
        try:
            horse_race = [r for r in self.horse_races if r.race_type == race_type][0]
        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")
        
        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        
        all_horses = [j.horse for j in horse_race.jockeys]
        winner = max(all_horses, key=lambda h: h.speed)
        winner_jockey  = [j for j in horse_race.jockeys if j.horse == winner][0]
        
        return f"The winner of the {race_type} race, with a speed of {winner.speed}km/h is {winner_jockey.name}! Winner's horse: {winner.name}."
            