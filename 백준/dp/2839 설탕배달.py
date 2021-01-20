

N = int(input())


def solution():
    dp = [9999 for _ in range(N+3)]
    dp[3] = 1
    dp[5] = 1

    for i in range(6, N+1):
        dp[i] = min(dp[i-3], dp[i-5]) + 1

    if dp[N] >= 9999:
        return -1
    else:
        return dp[N]
print(solution())

