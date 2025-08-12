def create_dict(keys, values):
    result = {}
    min_length = min(len(keys), len(values)) 

    for i in range(len(keys)):
        if i < min_length:
            result[keys[i]] = values[i]
        else:
            result[keys[i]] = None 

    return result