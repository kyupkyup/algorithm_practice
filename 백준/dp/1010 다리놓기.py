
T = int(input())
ans = []

def solution():
    global ans
    for _ in range(T):
        n, m = map(int, input().split(" "))
        ans = [1] * (m+n)
        print(dp(m) // (ans[m-n] * ans[n]))

        # print(dp(1, m) // ((dp(1, m-n)) * dp(1, n)))

def dp(m):
    global ans
    if m == 1:
        return 1
    elif ans[m] != 1:
        return ans[m]
    else:
        ans[m] = m * dp(m-1)
        return ans[m]

solution()