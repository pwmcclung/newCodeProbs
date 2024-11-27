def how_many_step(a, b):
    steps = 0
    if a == b:
        return 0
    while b > a:
        if b % 2 == 0 and b // 2 >= a:
            b //= 2
            steps += 1
        else:
            b -= 1
            steps += 1
    return steps