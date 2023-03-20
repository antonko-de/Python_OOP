class Integer:
    def __init__(self,value:int) -> None:
        self.value = value
        
    @classmethod
    def from_float(cls, floa_value:float):
        if not isinstance(floa_value, float):
            return f"value is not a float"
        return cls(int(floa_value))
    
    @classmethod
    def from_roman(cls,value:str):
        roman_dict = {
            "I" : 1,
        
            "V" : 5,
        
            "X" : 10, 
        
            "L" : 50,
            
            "C" : 100, 
            
            "D" : 500, 
    
            "M" : 1000
        }
        
        if len(value) == 1:
            return cls(roman_dict[value])
        
        total = 0
        for ind_char in range(len(value)):
            if  ind_char != 0 and roman_dict[value[ind_char]] > roman_dict[value[ind_char - 1]]:
                total += roman_dict[value[ind_char]] - 2 * roman_dict[value[ind_char - 1]]              
            else:
                total += roman_dict[value[ind_char]]
                
        return cls(total)
    
    @classmethod
    def from_string(cls, value:str):
        if not isinstance(value, str):
            return 'wrong type'
        
        return cls(int(value))
    

