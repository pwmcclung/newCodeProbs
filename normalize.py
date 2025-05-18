def normalize(arr, fill_value=None):
    if arr == []:
        return []
    length = len(max(arr, key=len))
    for x in arr:
        if len(x) != length:
            while len(x) != length:
                x.append(fill_value)
    return arr
