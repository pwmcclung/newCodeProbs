def is_in_middle(sequence):
    n = len(sequence)
    for i in range(n - 2):
        if sequence[i:i + 3] == "abc":
            left_len = i
            right_len = n - i - 3
            if abs(left_len - right_len) <= 1:
                return True
    return False