import math

def maximize_earnings(earnings, k):
    n = len(earnings)
    if n == 0:
        return 0

    dp = [[-1] * (k + 1) for _ in range(n)]

    dp[0][0] = 0  
    dp[0][1] = earnings[0] 

    for i in range(1, n):
        max_prev_earned = 0
        for j in range(k + 1):
            max_prev_earned = max(max_prev_earned, dp[i-1][j])
        dp[i][0] = max_prev_earned

        for j in range(1, k + 1):
            if dp[i-1][j-1] != -1:
                dp[i][j] = dp[i-1][j-1] + earnings[i]

    max_total_earned = 0
    for j in range(k + 1):
        max_total_earned = max(max_total_earned, dp[n-1][j])

    return max_total_earned