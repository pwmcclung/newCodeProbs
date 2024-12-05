def expected_value(r: int, c: int) -> int:
    if (r + 1) * (c + 1) == 0:
        return 0 
    total_sum = (r + 1) * (c + 1) * (r - c) // 2
    return total_sum // ((r + 1) * (c + 1))