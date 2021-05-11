import heapq

def kruskal(graph):
    mst = []
    heap = []
    for start_node in graph:
        for adj_node in start_node:
            heapq.heappush(heap, (adj_node[1], graph.index(start_node), adj_node[0]))

    list_set = []

    for i in range(len(graph)):
        list_set.append(i)

    while heap:
        distance, start, end = heapq.heappop(heap)
        root_a = find(start, list_set)
        root_b = find(end, list_set)

        if root_a != root_b:
            union(root_a,root_b, list_set)
            mst.append((distance,start,end))



    print(list_set)
    print(mst)

    return mst


def find(node, list_set):
    if node == list_set[node]:
        return node
    else:
        list_set[node] = find(list_set[node], list_set)
        return list_set[node]

def union(start, end, list_set):
    x = find(start, list_set)
    y = find(end, list_set)

    if x!=y:
        if x < y:
            list_set[y] = x
        else:
            list_set[x] = y


graph = [[(1, 28), (5, 10)],  # (인접노드, 가중치)
         [(0, 28), (2, 16), (6, 14)],
         [(1, 16), (3, 12)],
         [(2, 12), (4, 22), (6, 18)],
         [(3, 22), (5, 25), (6, 24)],
         [(0, 10), (4, 25)],
         [(1, 14), (3, 18), (4, 24)]]
kruskal(graph)