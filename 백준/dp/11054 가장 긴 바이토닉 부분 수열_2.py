N = int(input())
arr = list(map(int, input().split(" ")))


def solution():
    max_dp = [1] * N
    answer = -1
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                max_dp[i] = max(max_dp[i], max_dp[j] + 1)
    min_dp = [1] * N
    arr_re = arr[::-1]
    for k in range(N):
        for m in range(k):
            if arr_re[k] > arr_re[m]:
                min_dp[k] = max(min_dp[k], min_dp[m] + 1)

    for i in range(N):
        answer = max(answer, max_dp[i] + min_dp[::-1][i] - 1)
    print(answer)
solution()
