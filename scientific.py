def to_scientific(num):
    if num < 1000:
        return str(num)
    working_int = str(num)[0:4]
    length = 'e' + str(len(str(num)) -1)
    first = working_int[0] + '.'
    second = working_int[1:]
    if not second.endswith('5') and not second.endswith('0'):
        return first + second + length
    if second.endswith('5'):
        return first + second + length
    else:
        while second[1:].endswith('0'):
            second = second[:-1]
        return first + second + length