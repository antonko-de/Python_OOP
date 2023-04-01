'''Create a class called reverse_iter which should receive an iterable upon initialization. Implement the __iter__ and __next__ methods, 
so the iterator returns the items of the iterable in reversed order.'''


class reverse_iter:
    
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.range  = len(iterable) -1
        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.range >=0:
            curr = self.iterable[self.range]
            self.range -= 1
            return curr
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
