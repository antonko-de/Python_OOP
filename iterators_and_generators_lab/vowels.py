'''Create a class called vowels, which should receive a string. 
Implement the __iter__ and __next__ methods, so the iterator returns only the vowels from the string.'''

#97, 101, 105, 111, 117


class vowels:
    def __init__(self, s):
        self.s = s
        self.vowels = "aeiouAEIOU"
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.s):
            char = self.s[self.index]
            self.index += 1
            if char in self.vowels:
                return char
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
