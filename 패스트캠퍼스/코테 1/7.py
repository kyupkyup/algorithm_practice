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


ans = dijkstra(0, [[(1, 3), (5, 1)],
[(3, 5), (0, 2)],
[(4, 3)],
[(1, 1)],
[(3, 6)],
[(3, 2)]])

if float('inf') in ans:
    print(-1)
else:
    print(max(ans))