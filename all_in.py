def numbers(*args):
    print(args)
    count = []
    for x in args:
        if isinstance(x, (int,float)) and not type(x) == bool:
            count.append(1)
        elif not isinstance(x, (int,float)):
            count.append(0)
    if sum(count) == len(args):
        return True
    else:
        return False