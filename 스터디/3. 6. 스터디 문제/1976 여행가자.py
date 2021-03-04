import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(N)]
spot = list(map(int, input().split(" ")))
visited = [False] * (N+1)
adj_list = [[] for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        if arr[j][i] == 1 or i == j:
            adj_list[j].append(i)
            adj_list[i].append(j)


def solution():

    for i in range(N):
        for j in range(N):
            if arr[j][i] == 1:
                dfs(i, j)

    for i in spot:
        if not visited[i-1]:
            print("NO")
            return
    print("YES")

def dfs(i, j):
    for v in adj_list[i]:
        if not visited[v]:
            visited[v] = True
            dfs(v, j)
    for k in adj_list[j]:
        if not visited[k]:
            visited[k] = True
            dfs(i, k)

solution()