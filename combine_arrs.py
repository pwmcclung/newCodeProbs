def combine(*args):
    result = []
    iters = [iter(arg) for arg in args]
    while iters: 
        for it in iters[:]: 
            try:
                result.append(next(it))
            except StopIteration:
                iters.remove(it) 
    return result