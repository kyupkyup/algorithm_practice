
N = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(N)]
adj = [[] for _ in range(N)]
ans = [[0 for _ in range(N)] for _ in range(N)]
visited = [False] * (N+1)


check = False
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            adj[i].append(j)

def solution():
    global check, visited
    for i in range(N):
        for j in range(N):
            check = False
            visited = [False] * (N+1)

            dfs(i, j)
            if check:
                ans[i][j] = 1
            else:
                ans[i][j] = 0

    for i in range(N):
        for j in range(N):
            if j == N-1:
                print(ans[i][j], end="")
                print("")
            else:
                print(ans[i][j], end=" ")

    return


def dfs(node, target_node):
    global check, visited
    for v in adj[node]:

        if v == target_node:
            check = True
            return

        elif not visited[v]:
            visited[v] = True
            dfs(v, target_node)

solution()
