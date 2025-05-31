def digit_all (x):
    digs = '0123456789'
    new_str = ''
    if type(x) != str:
        return 'Invalid input !'
    for spot in x:
        if spot in digs:
            new_str += spot
    return new_str
