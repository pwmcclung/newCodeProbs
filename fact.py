import math
def count(n):
    if n < 0:
        return 0  
    if n <= 1:
        return 1 
    fact = 0.5 * math.log10(2 * math.pi * n) + n * (math.log10(n) - math.log10(math.e))
    return int(fact) + 1