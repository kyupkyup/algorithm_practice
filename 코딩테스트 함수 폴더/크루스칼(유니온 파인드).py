def kruskal(graph):
    edges = set()
    for node, adj_list in enumerate(graph):
        for adj_node, weight in adj_list:
            if node < adj_node:
                edges.add((weight, adj_node, node))
            else:
                edges.add((weight, node, adj_node))
    edges = list(edges)
    edges.sort()

    parents = [i for i in range(len(graph))]
    rank = [0 for _ in range(len(graph))]

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])  # path compression
        return parents[x]

    def union(a, b):
        if rank[a] < rank[b]:  # union-by-rank
            parents[b] = a
        else:
            parents[a] = b

        if rank[a] == rank[b]:
            rank[a] += 1

    mst = []
    sum_weight = 0
    for edge in edges:
        weight, a, b = edge
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            union(root_a, root_b)
            mst.append(edge)
            sum_weight += weight

    print(sum_weight)
    return mst
