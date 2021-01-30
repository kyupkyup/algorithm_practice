
from collections import deque

M, N = map(int, input().split(" "))
arr = [list(map(int, input().split(" "))) for _ in range(N)]

def solution():

    dq = deque([])

    for i in range(M):
        for j in range(N):
            if arr[j][i] == 1:
                dq.append([[i,j], 0])

    while dq:
        temp, count = dq.popleft()

        right = temp[0]+1
        left = temp[0]-1
        up = temp[1]-1
        down = temp[1]+1

        if right < M:
            if arr[temp[1]][right] == 0:
                dq.append([[right, temp[1]], count + 1])
                arr[temp[1]][right] = 1

        if down < N:
            if arr[down][temp[0]] == 0:
                dq.append([[temp[0], down], count + 1])
                arr[down][temp[0]] = 1

        if left >= 0:
            if arr[temp[1]][left] == 0:
                dq.append([[left, temp[1]], count + 1])
                arr[temp[1]][left] = 1

        if up >= 0:
            if arr[up][temp[0]] == 0:
                dq.append([[temp[0], up], count + 1])
                arr[up][temp[0]] = 1

    for i in range(M):
        for j in range(N):
            if arr[j][i] == 0:
                print(-1)
                return
    print(count)

solution()
