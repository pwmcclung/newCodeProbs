def rad_ladies(name):
    name_list = list(name)
    new_name = ''
    not_allowed = '%$&/£?@0123456789'
    for char in name_list:
        if char  not in not_allowed:
            new_name += char.upper()
    return new_name
