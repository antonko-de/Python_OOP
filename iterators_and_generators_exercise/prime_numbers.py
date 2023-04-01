from functools import reduce


def get_primes(numbers:list):
    def factors(n):    
        return set(reduce(list.__add__, 
                    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
    return [x for x in numbers if len(factors(x)) == 1]

    

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))