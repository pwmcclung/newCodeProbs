def count_streets(streets, drivers):
    data = {k: i for i, k in enumerate(streets)}
    new_arr = []
    for x in drivers:
        new_arr.append(abs(data[x[0]] - data[x[1]])-1)
    return new_arr