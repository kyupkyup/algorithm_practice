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

graph = [
    [(2,5), (3,2)],
    [(3,5),(4,3)],
    [(0,3),(4,9)],
    [(0,10), (4,2)],
    [(2,13),(1,3)]
]
dijkstra(3, graph)
