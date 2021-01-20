
T = int(input())
ans = []

def solution():
    global ans
    for _ in range(T):
        n, m = map(int, input().split(" "))
        ans = [1 for i in range(m+1)]
        dp(n, m)
        print(ans)

def dp(i, m):
    global ans
    if i == m:
        return m
    elif ans[i] != 1:
        return ans[i]
    else:
        ans[i] = i * dp(i+1, m)


solution()