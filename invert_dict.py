def invert_hash(dictionary):
    ks = list(dictionary.values())
    vals = list(dictionary.keys())
    new_dict =  dict(zip(ks,vals))
    return new_dict
