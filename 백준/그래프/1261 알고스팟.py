import heapq
INF = int(1e9)
M, N = map(int, input().split(" "))

graph = [list(map(int, input())) for _ in range(N)]
q = []
distance = [[INF for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def solution():

    dijkstra((0,0))


    print(distance[N - 1][M - 1])


def dijkstra(start):
    heapq.heappush(q, (0, start))
    distance[start[1]][start[0]] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now[1]][now[0]] < dist:
            continue
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            else:
                cost = dist + graph[ny][nx]
                if cost < distance[ny][nx]:
                    distance[ny][nx] = cost
                    heapq.heappush(q, (cost, (nx, ny)))
solution()