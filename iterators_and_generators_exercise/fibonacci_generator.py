'''Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely. 
The first two numbers in the sequence are always 0 and 1. Each following Fibonacci number is created by the sum of the current number with the previous one.
Note: Submit only the function in the judge system
'''

def fibonacci():
    first, second = 0, 1
    
    while True:
        yield first
        first, second = second, first + second
        
        
generator = fibonacci()
for i in range(5):
    print(next(generator))

