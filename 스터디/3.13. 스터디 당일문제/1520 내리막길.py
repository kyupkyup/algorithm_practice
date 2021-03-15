import sys
from _collections import deque

input = sys.stdin.readline

m, n = map(int, input().split(" "))

arr = [list(map(int, input().split(" "))) for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0


def solution():


    temp_cnt = 0
    dq = deque([])

    for k in range(4):
        nx = 0 + dx[k]
        ny = 0 + dy[k]

        if 0 <= nx < n and 0 <= ny < m:
            if arr[ny][nx] < arr[0][0]:
                temp_cnt += 1

    visited[0][0] = temp_cnt
    dq.append([0, 0])

    while dq:
        temp_cnt = 0
        i, j = dq.popleft()

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[ny][nx] < arr[j][i]:
                    temp_cnt += 1
                    visited[ny][nx] = max(visited[j][i] + temp_cnt - 1, visited[j][i])
                    dq.append([nx, ny])

    print(visited[m-1][n-1])
    print(visited)
##


solution()
