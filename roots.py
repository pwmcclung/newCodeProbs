def perfect_roots(n):
    second = n ** (1/2)
    fourth = n ** (1/4)
    eigth  = n ** (1/8)
    if (second % 1 == 0 and fourth % 1 == 0 and eigth % 1 == 0):
        return True
    else:
        return False