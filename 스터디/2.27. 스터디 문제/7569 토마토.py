import sys
from _collections import deque
input = sys.stdin.readline

X, Y, Z = map(int, input().split(" "))
raped = [[[False for _ in range(X)] for _ in range(Y)] for _ in range(Z)]
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


arr = [[list(map(int, input().split(" "))) for _ in range(Y)] for _ in range(Z)]


def solution():
    global ans , X,Y,Z, arr, raped
    dq = deque([])
    ans = 0

    for z in range(Z):
        for y in range(Y):
            for x in range(X):
                if arr[z][y][x] == 1:
                    raped[z][y][x] = True
                    dq.append([[x, y, z], 0])

    while dq:
        point, count = dq.popleft()
        for k in range(6):
            nx = point[0] + dx[k]
            ny = point[1] + dy[k]
            nz = point[2] + dz[k]
            if 0 <= nx < X and 0 <= ny < Y and 0 <= nz < Z:
                if arr[nz][ny][nx] == 0 and not raped[nz][ny][nx]:
                    raped[nz][ny][nx] = True
                    arr[nz][ny][nx] = 1
                    dq.append([[nx, ny, nz], count + 1])
        ans = max(count, ans)

    for z in range(Z):
        for y in range(Y):
            for x in range(X):
                if arr[z][y][x] == 0:
                    print(-1)
                    return
    print(ans)
solution()