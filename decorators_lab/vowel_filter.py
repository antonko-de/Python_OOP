def vowel_filter(function):

    def wrapper():
        vowels = ["a", "e", "i", "o", "u"]
        result = function()
        
        return [x for x  in result if x in vowels]

    return wrapper


