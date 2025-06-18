def count_set_bits(n):
    count = 0
    while n > 0:
        n &= (n - 1)  
        count += 1
    return count

def sort_by_bit(arr):
    arr.sort(key=lambda n: (count_set_bits(n), n))