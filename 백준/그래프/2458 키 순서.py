N, M = map(int, input().split(" "))
INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]



def solution():
    for i in range(1, N+1):
        graph[i][i] = 1


    for i in range(M):
        a, b = map(int, input().split(" "))
        graph[a][b] = 1


    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if graph[j][k] + graph[k][i] < INF:
                    graph[j][i] = 1

    check = True
    ans = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] == INF and graph[j][i] == INF:
                check = False
                break
        if check:
            ans += 1
        check = True
    print(ans)
solution()

