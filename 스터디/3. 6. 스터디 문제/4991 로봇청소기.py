import sys
from _collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(w, h, arr):
    visited = [[False for _ in range(w)] for _ in range(h)]
    dirt_spot = 0
    ans = 0
    dq = deque([])
    for j in range(h):
        for i in range(w):
            if arr[j][i] == "*":
                dirt_spot += 1
            if arr[j][i] == "o":
                arr[j][i] = "."
                visited[j][i] = True
                dq.append([i, j, 0])
    while dq:
        x, y, count = dq.popleft()
        if dirt_spot <= 0:
            print(count)
            return

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
                if arr[ny][nx] == "*":
                    arr[ny][nx] = "."
                    dirt_spot -= 1
                    dq.clear()
                    visited = [[False for _ in range(w)] for _ in range(h)]
                    visited[ny][nx] = True
                    dq.append([nx, ny, count + 1])
                elif arr[ny][nx] == "x":
                    continue
                else:
                    visited[ny][nx] = True
                    dq.append([nx, ny, count + 1])

    if dirt_spot > 0:
        print(-1)


while True:
    w, h = map(int, input().split(' '))
    arr = [list(input()) for _ in range(h)]

    if w == 0 and h == 0:
        break
    solution(w, h, arr)
