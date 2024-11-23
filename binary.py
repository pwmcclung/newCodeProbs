def ones_complement(binary_number):
    return ''.join('1' if bit == '0' else '0' for bit in binary_number)