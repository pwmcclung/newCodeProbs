def array_info(x):
## the code isn't gonna write itself!
    if len(x) == 0:
        return 'Nothing in the array!'
    length  = len(x)
    num_int = 0
    num_float = 0
    num_str = 0
    num_white = 0
    for item in x:
        if type(item) == int:
            num_int += 1
        if type(item) == float:
            num_float += 1
        if str(item).isalpha():
            num_str += 1
        if str(item).isspace():
            num_white += 1
    if num_int == 0:
        num_int = None
    if num_float == 0:
        num_float = None
    if num_str == 0:
        num_str = None
    if num_white == 0:
        num_white = None
    return [[length],[num_int],[num_float],[num_str],[num_white]]