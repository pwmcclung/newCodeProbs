import math
def cyclops(n):
    binary_rep = bin(n)[2:]
    if len(binary_rep) < 3:
        return False
    elif len(binary_rep) % 2 == 0:
        return False
    else:
        o_list = [x for x in binary_rep if x == '0']
        mid = len(binary_rep) // 2
        if binary_rep[mid] == '0' and len(o_list) == 1:
            return True
        else:
            return False
        