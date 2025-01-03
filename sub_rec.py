def has_subpattern(strng):
    n = len(strng)
    for i in range(1, n // 2 + 1):  
        if n % i == 0:  
            subpattern = strng[:i]
            repeated = subpattern * (n // i)
            if repeated == strng:
                return True
    return False