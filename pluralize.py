def pluralize(word):
    cons = 'bcdfghjklmnpqrstvwxyz'
    if word[-1] == 's' or word[-1] == 'x' or word[-1] == 'z' or word[-2:] == 'ch' or word[-2:] == 'sh':
        return word + 'es'
    elif word[-2] in cons and word[-1] == 'y':
        return word[:-1] + 'ies'
    else:
        return word + 's'
