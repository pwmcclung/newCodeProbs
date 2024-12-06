def get_matrix(n):
    identity_mat = [[0] * i + [1] + [0] * (n - i - 1) for i in range(n)]
    return identity_mat