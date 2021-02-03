N, M = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(M)]
visited = [False] * N+1


def solution():
    visited[graph[0][0]] = True
    count = 1
    while True:
        dfs(graph[0])
        count += 1


def dfs(edge):
    for i in graph:
        if i[0] == edge[1]:
            if not visited[edge[1]]:
                check = True
                visited[i[1]] = True
                dfs(edge[1])
        else:
            continue

    return


solution()