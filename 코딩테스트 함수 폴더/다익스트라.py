
import heapq

def dijkstra(start, graph):
    n = len(graph)
    heap = []
    heapq.heapify(heap)
    distances = [float('inf')] * n

    for node in range(n):
        if node == start:
            heapq.heappush(heap, [start, 0])
            while heap:
                curr = heapq.heappop(heap)
                if curr[1] < distances[curr[0]]:
                    distances[curr[0]] = curr[1]
                for adj_node in graph[curr[0]]:
                    if curr[1]+ adj_node[1] < distances[adj_node[0]]:
                        distances[adj_node[0]] = curr[1] + adj_node[1]
                        heapq.heappush(heap, (adj_node[0], curr[1] + adj_node[1]))

    print(distances)