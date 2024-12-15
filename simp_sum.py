def simple_sum(x, y):
    while y:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x