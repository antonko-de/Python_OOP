
class Profile:
    
    def __init__(self, username:str, password:str) -> None:
        
        self.username = username
        self.password = password
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, val):
        
        if 5 <= len(val) <= 15:
            self.__username = val
            
        else:
            raise ValueError("The username must be between 5 and 15 characters.")
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, val:str):
        if len(val) < 8 or not any(x.isdigit() for x in val)  or not any(i.isupper() for i in val):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        
        self.__password = val
        
    def __str__(self) -> str:
        return f"You have a profile with username: \"{self.__username}\" and password: {'*' * len(self.__password)}"
    


