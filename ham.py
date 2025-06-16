def hamming_weight(x):
    bin_x = bin(x)[2:]
    sum_1 = sum([int(x) for x in bin_x if x == '1'])
    return sum_1