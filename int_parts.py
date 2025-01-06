def partitions(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1

    dp = [0] * (n + 1)  
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]