import bisect

def array_manip(array):
    n = len(array)
    result = []
    sorted_array = [] 

    for i in range(n - 1, -1, -1):
        current_element = array[i]
        insertion_point = bisect.bisect_left(sorted_array, current_element + 1)

        if insertion_point < len(sorted_array):
            result.insert(0, sorted_array[insertion_point])
        else:
            result.insert(0, -1) 
        bisect.insort(sorted_array, current_element)

    return result