def trim(beard):
    end = beard[-1]
    new_end = ['...' for x in end]
    new_beard = []
    for x in beard:
        new_x = ['|' if x == 'J' else x for x in x]
        new_beard.append(new_x)
    return new_beard[0:-1]+[new_end]