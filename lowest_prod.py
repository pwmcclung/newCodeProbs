def lowest_product(num):
    if len(num) < 4:
        return "Number is too small"

    min_product = float('inf')  
    for i in range(len(num) - 3):
        product = 1
        for j in range(i, i + 4):
            product *= int(num[j])
        min_product = min(min_product, product)

    return min_product