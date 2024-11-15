def calculate_probability(n):
    accum = 1
    x = 1
    while x < n:
        accum *= 1 - x / 365
        x += 1
    return round((1-accum) * 100) / 100