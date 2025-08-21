import math

def choose(n, k):
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    if k > n // 2:
        k = n - k  

    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)  
    return result