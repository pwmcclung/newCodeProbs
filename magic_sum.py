def magic_sum(arr):
    summed = 0
    for x in arr:
        if '3' in str(x) and x % 2 != 0:
            summed += x
    return summed
