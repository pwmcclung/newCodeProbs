def hamming_distance(a, b):
    new_a = format(a, '08b')
    new_b = format(b, '08b')
    if len(new_a) < len(new_b):
        new_a = new_a.zfill(len(new_b))
    if len(new_b) < len(new_a):
        new_b = new_b.zfill(len(new_a))
    return sum(c1 != c2 for c1, c2 in zip(new_a, new_b))