def min_value(arr, n):
    new_arr = []
    while len(arr) >= n:
        window = [arr[0:n]]
        smallest = min(window)
        new_arr.append(smallest)
        arr.pop(0)
    arr1 = [min(x) for x in new_arr]
    return arr1