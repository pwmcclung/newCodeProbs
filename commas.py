def number_format(n):
    count = 0
    arr  = [x for x in str(n)]
    start = len(arr)
    new_arr = []
    while start > 0:
        item = arr.pop()
        new_arr.insert(0,item)
        count += 1
        if count == 3:
            new_arr.insert(0, ',')
            count = 0
        start = start - 1
    if new_arr[0] == ',':
        new_arr.pop(0)
    if new_arr[0] == '-' and new_arr[1] == ',':
        new_arr.pop(1)
    return ''.join(new_arr)