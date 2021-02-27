import sys
import heapq

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
start = [0,0]

for i in range(N):
    for j in range(N):
        if arr[j][i] == 9:
            start[0], start[1] = i, j
            arr[j][i] = 0

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

def solution():
    global N, arr, start, dx, dy, visited
    shark = 2
    count = 0
    ans = 0
    heap = []
    heapq.heappush(heap, [0, start[1], start[0]])
    visited[start[1]][start[0]] = True

    while heap:
        timer, y, x = heapq.heappop(heap)

        if 0 < arr[y][x] < shark:
            ans = timer
            count += 1
            if shark == count:
                count = 0
                shark += 1
            arr[y][x] = 0
            heap = []
            visited = [[False for _ in range(N)] for _ in range(N)]
            visited[y][x] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if 0 <= arr[ny][nx] <= shark:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        heapq.heappush(heap, [timer + 1, ny, nx])
    print(ans)





solution()