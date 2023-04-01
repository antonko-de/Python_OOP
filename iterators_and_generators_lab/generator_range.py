'''Create a generator function called genrange that receives a start (int) and an end (int) upon initialization. 
It should generate all the numbers from the start to the end (inclusive).'''


def genrange(start:int, end:int):
    
    for num in range(start, end + 1):
        yield num
        

print(list(genrange(1, 10)))