class Concert:
    
    POSSIBLE_GENRES = ["Metal", "Rock", "Jazz"]
    
    
    def __init__(self, genre:str, audience:int, ticket_price:float, expenses:float, place:str) -> None:
        self.genre = genre
        self.audience  = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place =  place
        
    
    @property
    def genre(self) -> str:
        return self.__genre
    
    @genre.setter
    def genre(self, val:str) -> None:
        if not val in Concert.POSSIBLE_GENRES:
            raise ValueError(f"Our group doesn't play {val}!")
        
        self.__genre = val
        
    @property
    def audience(self) -> int:
        return self.__audience
    
    @audience.setter
    def audience(self, val:int) -> None:
        if val < 1:
            raise ValueError("At least one person should attend the concert!")
        
        self.__audience = val
        
    @property
    def ticket_price(self) -> float:
        return self.__ticket_price
    
    @ticket_price.setter
    def ticket_price(self, val:float) -> None:
        if val < 1.0:
            raise ValueError("Ticket price must be at least 1.00$!")
        
        self.__ticket_price = val
        
    @property
    def expenses(self) -> float:
        return self.__expenses
    
    @expenses.setter
    def expenses(self, val:float) -> None:
        if val < 0.00:
            raise ValueError("Expenses cannot be a negative number!")
        
        self.__expenses = val
        
    @property
    def place(self) -> str:
        return self.__place
    
    @place.setter
    def place(self, val:str) -> None:
        if val.strip() == "" or len(val) < 2:
            raise ValueError("Place must contain at least 2 chars. It cannot be empty!")
        
        self.__place = val
        
    def __str__(self) -> str:
        return f"{self.genre} concert at {self.place}."
    