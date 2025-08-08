import math
def solution(lst):
    X = lst
    if not X:
        return 0 

    gcd_val = X[0]
    for i in range(1, len(X)):
        gcd_val = math.gcd(gcd_val, X[i])

    return gcd_val * len(X)