N = int(input())
arr = list(map(int, input().split(" ")))

def solution():
    max_dp = [1] * N
    min_dp = [1] * N

    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                max_dp[i] = max(max_dp[i], max_dp[j]+1)
                for k in range(j+1, N):
                    for m in range(k):
                        if arr[k] < arr[m]:
                           min_dp[k] = max(min_dp[k], min_dp[m]+1)

    print(max_dp)
    print(min_dp)

solution()