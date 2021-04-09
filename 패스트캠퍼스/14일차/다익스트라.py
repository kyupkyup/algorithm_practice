
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


    # for node in range(n):
    #     if node == start:
    #         heapq.heappush(heap, [start, 0])
    #         while heap:
    #             curr = heapq.heappop(heap)
    #             if curr[1] < distances[curr[0]]:
    #                 distances[curr[0]] = curr[1]
    #             for adj_node in graph[curr[0]]:
    #                 if curr[1]+ adj_node[1] < distances[adj_node[0]]:
    #                     distances[adj_node[0]] = curr[1] + adj_node[1]
    #                     heapq.heappush(heap, (adj_node[0], curr[1] + adj_node[1]))
    #
    # print(distances)


graph = [[(2, 5), (3, 2)], # (인접노드, 가중치)
         [(3, 5), (4, -3)],
         [(0, 3), (4, -9)],
         [(0, 10), (4, 2)],
         [(2, 13), (1, 3)]]

dijkstra(3, graph)

