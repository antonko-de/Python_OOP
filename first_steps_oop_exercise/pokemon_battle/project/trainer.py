'''The Trainer class should receive a name (string). The Trainer should also have an attribute pokemons (list, empty by default).
The Trainer has three methods:
-	add_pokemon(pokemon: Pokemon)
o	Adds the pokemon to the collection and returns "Caught {pokemon_name} with health {pokemon_health}". Hint: use the pokemon's details method.
o	If the pokemon is already in the collection, returns "This pokemon is already caught"
o	Hint: to import the Pokemon class, you should add "from project.pokemon import Pokemon"
-	release_pokemon(pokemon_name: string) 
o	Checks if you have a pokemon with that name and removes it from the collection. In the end, returns "You have released {pokemon_name}"
o	If there is no pokemon with that name in the collection, returns "Pokemon is not caught"
-	trainer_data()
o	The method returns the information about the trainer and his pokemon's collection in the format:
"Pokemon Trainer {trainer_name}
 Pokemon count {the amount of pokemon caught}
 - {pokemon_details1}
 ...
 - {pokemon_detailsN}"
'''
from project.pokemon import Pokemon

class Trainer:
    
    def __init__(self, name:str) -> None:
        self.name = name
        self.pokemons = []
        
    
    def add_pokemon(self, pokemon:Pokemon) -> str:
        if not pokemon in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return f"This pokemon is already caught"
        
    def release_pokemon(self, pokemon_name)-> str:
        for poke in self.pokemons:
            if pokemon_name == poke.name:
                self.pokemons.remove(poke)
                return f"You have released {pokemon_name}"
                
        return f"Pokemon is not caught"
    
    def trainer_data(self)->str:
        output = ""
        output += f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for poke in self.pokemons:
            output += "- " + poke.pokemon_details() + '\n'
            
        return output
    
    

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())


        
    