# 크루스칼 알고리즘

import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

edges = []
result = 0

parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    a, b, cost = map(int, input().split(" "))
    edges.append((cost, a, b))

edges.sort()


def kruscal():
    global result, edges, parent
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    print(result)

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
kruscal()