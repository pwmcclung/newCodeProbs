import math
def solution(n):
    x2 = n * 2
    lower = math.floor(x2) / 2
    upper = math.ceil(x2) / 2

    if abs(n - lower) <= abs(n-upper):
        if abs(n - lower) == abs(n - upper): 
            return upper
        else:
            return lower

    else:
        return upper