def merge(line):
    # 1. Remove zeros and store the number of trailing zeros
    trailing_zeros = 0
    non_zeros = []
    for x in reversed(line):
        if x == 0:
            trailing_zeros += 1
        else:
            non_zeros.insert(0, x) # insert at the beginning to maintain order
        
    # 2. Initialize result list
    merged_line = []

    # 3. Loop through non zero tiles to merge
    i = 0
    while i < len(non_zeros):
        # 4. if a next item exists and is equal, merge
        if i + 1 < len(non_zeros) and non_zeros[i] == non_zeros[i+1]:
            merged_line.append(non_zeros[i] * 2)
            i += 2
        else:
            merged_line.append(non_zeros[i])
            i += 1

    # 5. Add trailing zeros
    merged_line.extend([0] * trailing_zeros)
    #6. Add remaining zeros to reach len(line)
    num_zeros = len(line) - len(merged_line)
    merged_line.extend([0]*num_zeros)
    return merged_line