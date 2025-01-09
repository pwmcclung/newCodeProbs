def compute_depth(n):
    digits_found = set()
    multiple_count = 0
    
    while len(digits_found) < 10:
        multiple_count += 1
        multiple = n * multiple_count
        for digit in str(multiple):
            digits_found.add(digit)

    return multiple_count