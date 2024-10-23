def colour_association(arr):
    new_arr = []
    for x in range(len(arr)):
        new_arr.append({arr[x][0]: arr[x][1]})
    return new_arr