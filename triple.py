def triple_shiftian(base,n):
    if len(base) != 3 or n < 0:
        raise ValueError("Invalid input. Base must be a list of length 3 and n must be non-negative.")

    if n <= 2:
        return base[n]

    T = base[:]  
    for i in range(3, n + 1):
        next_val = 4 * T[i - 1] - 5 * T[i - 2] + 3 * T[i - 3]
        T.append(next_val)

    return T[n]