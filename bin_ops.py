def flip_bit(value, bit_index):
    mask = 1 << (bit_index - 1) 
    return value ^ mask  