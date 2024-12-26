def all_non_consecutive(arr):
    if len(arr) <= 1:
        return []

    result = []
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            result.append({'i': i, 'n': arr[i]})
    return result