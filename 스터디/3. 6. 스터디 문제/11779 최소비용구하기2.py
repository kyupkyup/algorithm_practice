import sys, heapq, copy
input = sys.stdin.readline
inf = int(1e9)
n = int(input())
m = int(input())

arr = [list(map(int, input().split(' '))) for _ in range(m)]
start, end = map(int, input().split(' '))
adj = [[] for _ in range(n+1)]
path = [[] for _ in range(n+1)]
distance = [inf] * (n+1)

for start1, end1, cost in arr:
    adj[start1].append([end1, cost])

def solution():
    global start, end, arr, adj, distance
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    ans = []
    temp = []
    while q:
        dist, now = heapq.heappop(q)
        temp.append(now)
        if distance[now] < dist:
            continue
        path[now].append(now)
        for i in adj[now ]:
            temp.append(i[0])
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
                path[i[0]] = copy.deepcopy(path[now])

    print(distance[end])
    print(len(path[end]))
    for i in path[end]:
        print(i, end=" ")


solution()
