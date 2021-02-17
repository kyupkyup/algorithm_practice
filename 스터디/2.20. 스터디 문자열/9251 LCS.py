
S1 = list(input())
S2 = list(input())
S1.insert(0,0)
S2.insert(0,0)

len1 = len(S1)
len2 = len(S2)


dp = [[0] * (len1) for _ in range(len2)]
def solution():
    for j in range(1, len2):
        for i in range(1, len1):
            if S1[i] == S2[j]:
                if dp[j-1][i] <= i-1 and dp[j][i-1] <= j-1:
                    dp[j][i] = dp[j-1][i-1] + 1
                else:
                    dp[j][i] = max(dp[j][i - 1], dp[j-1][i])
            else:
                dp[j][i] = max(dp[j][i - 1], dp[j-1][i])
0

    print(dp[len2-1][len1-1])
solution()