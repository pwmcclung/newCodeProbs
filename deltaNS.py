def delta(values, n): 
    if n <= 0:
        raise ValueError("Level must be a positive integer.")

    def generate_differences(iterable, level):
        if level == 1:
            it = iter(iterable)
            try:
                prev = next(it)
            except StopIteration:
                return  
            for curr in it:
                yield curr - prev
                prev = curr
        else:
            previous_level = generate_differences(iterable, level -1)
            try:
                prev = next(previous_level)
            except StopIteration:
                return 
            for curr in previous_level:
                yield curr - prev
                prev = curr
            

    return generate_differences(values, n)