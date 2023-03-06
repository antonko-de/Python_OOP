'''The Guild class receives a name (string). The Guild should also have one instance attribute players (an empty list which will contain the players of the guild). 
The class also has 3 additional methods:
-	assign_player(player: Player)
o	Adds the player to the guild and returns "Welcome player {player_name} to the guild {guild_name}". Remember to change the player's guild in the player class.
o	If he is already in the guild, returns "Player {player_name} is already in the guild."
o	If the player is in another guild, returns "Player {player_name} is in another guild."
-	kick_player(player_name: str)
o	Removes the player from the guild and returns "Player {player_name} has been removed from the guild.". Remember to change the player's guild in the player class to "Unaffiliated".
o	If there is no such player in the guild, returns "Player {player_name} is not in the guild."
-	guild_info() 
o	Returns the guild's information, including the players in the guild, in the format:
"Guild: {guild_name}
{first_player's info}
…
{Nplayer's info}"
'''
from project.player import Player

class Guild:
    
    def __init__(self, name:str) -> None:
        self.name = name
        self.players:list = []
        
    def assign_player(self, player:Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        
        elif not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."
            
        
        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"
    
    def kick_player(self,player_name:str) -> str:
        try:
            player = next(filter(lambda p: p.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."
        
        
        self.players.remove(player)
        player.guild = 'Unaffiliated'
        return f"Player {player_name} has been removed from the guild."
        
    
    def guild_info(self):
        output = f"Guild: {self.name}\n"
        
        for player in self.players:
            output += player.player_info() + "\n"
            
        return output
            
            

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
