'''Create a generator function called reverse_text that receives a string and yields all string characters on one line in reversed order.'''

def reverse_text(text:str):
    reversed_text = text[::-1]
    for i in reversed_text:
        yield i
        

for char in reverse_text("step"):
    print(char, end='')
