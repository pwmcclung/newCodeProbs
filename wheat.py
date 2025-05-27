import math

def squares_needed(grains):
    if grains <= 0:
        return 0
    n = math.ceil(math.log2(grains + 1))  
    return n