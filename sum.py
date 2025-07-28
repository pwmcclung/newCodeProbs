def closing_in_sum(n):
    list_n = [int(digit) for digit in str(n)]
    arr = []
    if len(list_n) % 2 == 0:
        while len(list_n) > 0:
            first = str(list_n.pop(0))
            second = str(list_n.pop())
            arr.append(first+second)
    else:
        while len(list_n) > 1:
            first = str(list_n.pop(0))
            second = str(list_n.pop())
            arr.append(first+second)
        arr.append(list_n[0])      
    sum_arr = sum([int(x) for x in arr])
    return sum_arr