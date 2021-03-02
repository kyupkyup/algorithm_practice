import sys
from _collections import deque

input = sys.stdin.readline

N, M = map(int, input().split(" "))

arr = [list(input()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
real_ans = 10000000


def solution():
    global count, arr, N, M, ans, visited
    dq = deque([])
    count = 0
    for j in range(N):
        for i in range(M):
            if arr[j][i] == "L":

                visited = [[False for _ in range(M)] for _ in range(N)]
                visited[j][i] = True
                dq.append([i, j, 0])
            while dq:
                x, y, count = dq.popleft()
                ans = max(ans, count)
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < M and 0 <= ny < N:
                        if arr[ny][nx] == "L" and not visited[ny][nx]:
                            dq.append([nx, ny, count+1])
                            visited[ny][nx] = True

    print(ans)


solution()
