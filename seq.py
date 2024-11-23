def find_missing_number(sequence):
    if len(sequence) == 0:
        return 0
    try:
        elements = [int(x) for x in sequence.split()]
    except ValueError:
        return 1  
    elements_set = set(elements) 
    max_element = max(elements)
    missing_numbers = set(range(1, max_element + 1)) - elements_set
    if not missing_numbers:
        return 0  
    else:
        return min(missing_numbers)