def shared_bits(a, b):
    shared = a & b
    
    count = bin(shared).count('1')
    
    return count >= 2