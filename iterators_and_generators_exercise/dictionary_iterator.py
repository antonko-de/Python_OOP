''''Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object. 
Implement the iterator to return each key-value pair of the dictionary as a tuple of two elements (the key and the value).
Note: Submit only the class in the judge system
'''


class dictionary_iter:
    
    def __init__(self, dictionary:dict) -> None:
        self.dictionary = list(dictionary.items())
        self.range = len(dictionary) -1
        self.index = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.index >= self.range:
            raise StopIteration
        
        self.index += 1
        return self.dictionary[self.index]
        

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
