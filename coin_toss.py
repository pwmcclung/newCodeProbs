def coin(n):
    result = []
    for i in range(2**n):
        binary = bin(i)[2:].zfill(n)
        s = ""
        for bit in binary:
            if bit == '0':
                s += 'H'
            else:
                s += 'T'
        result.append(s)
    return result