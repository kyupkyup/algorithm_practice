import heapq
INF = int(1e9)
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split(" "))
    graph[a].append((b, c))

start, end = map(int, input().split(" "))
distance = [INF] * (N+1)
q = []

def solution():
    dijkstra(start)
    print(distance[end])

def dijkstra(start):
    heapq.heappush(q, (0, start)) # 시작점 cost 0 초기화 및 start 넣어줌
    distance[start] = 0 #distance 배열의 스타트는 0

    while q:
        dist, now = heapq.heappop(q) # 현재 가장 경로가 짧은 노드를 꺼냄

        if distance[now] < dist: # 현재까지 계산된 최소경로비용
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


solution()