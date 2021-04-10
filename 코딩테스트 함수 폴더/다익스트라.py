import heapq

def dijkstra(start, graph):
    n = len(graph)
    heap = []
    heapq.heapify(heap)
    distances = [float('inf')] * n

    heapq.heappush(heap, (0, start))
    distances[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)

        if distances[node] < dist:
            continue
        adj_list = graph[node]
        for adj_node, adj_dist in adj_list:
            new_dist = dist + adj_dist
            if distances[adj_node] > new_dist:
                distances[adj_node] = new_dist
                heapq.heappush(heap, (new_dist, adj_node))
    return distances

# 다익스트라 재귀
def dijkstra_recur(start, graph):
    distList = [float('inf')] * len(graph)
    h = []

    heapq.heappush(h, (0, start))
    distList[start] = 0

    def recur(nodeIdx):
        dist, node = heapq.heappop(h)

        if dist > distList[node]:
            return

        for v, w in graph[nodeIdx]:
            if dist + w < distList[v]:
                distList[v] = dist + w
                heapq.heappush(h, (dist+w, v))
                recur(v)

    recur(start)

    return distList

def dijkstra_path(start, graph):
    n = len(graph)
    heap = []
    distances = [[float('inf'),[None]]] * n
    distances[start] = [0,[start]]
    heapq.heappush(heap, (0, [start])) # dist=0, node=start

    while heap: # len(heap) != 0
        select_dist, select_path = heapq.heappop(heap)
        select_node = select_path[-1]
        if select_dist > distances[select_node][0]:
            continue

        for adj_node, adj_dist in graph[select_node]: # 인접노드들 계산
            new_dist = select_dist + adj_dist
            if new_dist < distances[adj_node][0]:
                new_path = select_path[:]
                new_path.append(adj_node)
                distances[adj_node] = [new_dist, new_path] # 업데이트 할 때는 heap과 distance에 같이 넣어준다.
                heapq.heappush(heap, (new_dist, new_path))

    return distances

graph = [[(2, 5), (3, 2)], # (인접노드, 가중치)
         [(3, 5), (4, 4)],
         [(0, 3), (4, 5)],
         [(0, 10), (4, 2)],
         [(2, 13), (1, 3)]]


print(dijkstra_path(0,graph ))
