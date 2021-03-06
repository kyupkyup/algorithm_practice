import sys
from _collections import deque

input = sys.stdin.readline

H, W = map(int, input().split(" "))

arr = [list(input()) for _ in range(H)]
dot_arr = [[0 for _ in range(W)] for _ in range(H)]
gone = [[False for _ in range(W)] for _ in range(H)]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def solution():
    ans = 0
    dq = deque([])
    for j in range(H):
        for i in range(W):
            count = 0
            if arr[j][i] != ".":
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < W and 0 <= ny < H:
                        if arr[ny][nx] == ".":
                            count += 1
                if int(arr[j][i]) <= count:
                    dq.append([i, j, 0])
            dot_arr[j][i] = count

    while dq:
        i, j, count = dq.popleft()

        if dot_arr[j][i] >= int(arr[j][i]) and not gone[j][i]:
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < W and 0 <= ny < H:
                    if arr[ny][nx] != ".":
                        dot_arr[ny][nx] += 1
                        if dot_arr[ny][nx] >= int(arr[ny][nx]):
                            gone[j][i] = True
                            dq.append([nx, ny, count + 1])

        ans = max(ans, count)
    print(ans)


solution()
