def avg_array(arrs):
    if not arrs:  
        return []

    num_arrays = len(arrs)
    array_length = len(arrs[0])  

    if not all(len(arr) == array_length for arr in arrs):
        raise ValueError("All inner arrays must have the same length.")

    averages = []
    for i in range(array_length):
        sum_at_index = sum(arrs[j][i] for j in range(num_arrays))
        avg = sum_at_index / num_arrays
        averages.append(avg)

    return averages