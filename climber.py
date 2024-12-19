def climb(n):
    result = []
    current = n
    while current > 0:
        result.append(current)
        if current % 2 == 0:
            current //= 2  
        else:
            current = (current - 1) // 2
    result.reverse()  
    return result