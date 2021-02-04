N, M = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(M)]
visited = [False] * (N+1)
count = 0
adj = [[] for _ in range(N+1)]

for n, m in graph:
    adj[n].append(m)
    adj[m].append(n)

def solution():
    global count
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            count += 1
            dfs(i)
    print(count)

def dfs(node):
    for i in adj[node]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
    return

solution()