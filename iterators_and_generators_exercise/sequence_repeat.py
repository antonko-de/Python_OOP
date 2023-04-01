'''Create a class called sequence_repeat which should receive a sequence and a number upon initialization. Implement an iterator to return the given elements, 
so they form a string with a length - the given number. If the number is greater than the number of elements, 
then the sequence repeats as necessary. For more clarification, see the examples:'''


class sequence_repeat:
    
    def __init__(self, sequence, number:int) -> None:
        self.sequence = sequence
        self.number = number
        self.range = len(sequence) - 1
        self.index = -1
        self.counter = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter >= self.number:
            raise StopIteration
        
        if self.index >= self.range:
            self.index = -1
        
        self.counter +=1
        self.index +=1
            
        return self.sequence[self.index]        


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
