def eliminate_unset_bits(number):
    binary_string = "".join(x for x in number if x == '1')  
    if not binary_string: 
        return 0
    return int(binary_string, 2)