def f(x, a, b, c): 
    value_map = {a: b, b: c, c: a}
    return value_map.get(x, x)