import sys
sys.setrecursionlimit(15000)
input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False for _ in range(N)] for _ in range(N)]
def solution():
    global visited, arr
    ans = 0

    for height in range(1, 101):
        visited = [[False for _ in range(N)] for _ in range(N)]
        count = 0
        for i in range(N):
            for j in range(N):
                if arr[j][i] >= height and not visited[j][i]:
                    dfs(height, i, j)
                    count += 1

        ans = max(ans, count)
    print(ans)
def dfs(height, k, j):
    global visited, dx, dy
    for i in range(4):
        nx = k + dx[i]
        ny = j + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[ny][nx] >= height and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(height, nx, ny)

    return
solution()
