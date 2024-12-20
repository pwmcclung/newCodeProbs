def is_triangular(t):
    i = 1
    while i * (i + 1) // 2 < t:
        i += 1

    return i * (i + 1) // 2 == t