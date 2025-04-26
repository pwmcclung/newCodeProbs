def even_twins(numbers):
    arr = []
    while len(numbers) != 0:
        first = numbers.pop(0)
        for x in numbers:
            arr.append(first + x)
    new_arr = [x for x in arr if x % 2 == 0]
    return len(set(new_arr))
