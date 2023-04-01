def read_next(*args):
    
    elements = args
    
    for el in elements:
        for i in el:
            yield i
            
    
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
        
    