import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))

arr = [list(map(int, list(input().strip()))) for _ in range(n)]
ans = [[0 for _ in range(m+1)] for _ in range(n+1)]

def solution():
    ans_max = 0
    for j in range(1, n+1):
        for i in range(1, m+1):
            if arr[j-1][i-1] == 1:
                ans[j][i] = min(ans[j-1][i], ans[j][i-1], ans[j-1][i-1])+1
            ans_max = max(ans[j][i], ans_max)
    print(ans_max ** 2)



solution()