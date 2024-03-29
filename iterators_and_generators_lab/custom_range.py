'''Create a class called custom_range that receives a start (int) and an end (int) upon initialization. 
Implement the __iter__ and __next__ methods, so the iterator returns the numbers from the start to the end (inclusive).'''

class custom_range:
    
    def __init__(self, start:int, end:int) -> None:
        self.start = start
        self.end = end
        
    
    def __iter__(self):
        
        return self
    
    def __next__(self):
        if self.start <= self.end:
            curr = self.start
            self.start += 1
            return curr
        else:
            raise StopIteration