import sys
from _collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(" "))
arr = [list(input()) for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution():

    red_dq = deque([])
    blue_dq = deque([])

    for j in range(M):
        for i in range(N):
            if arr[j][i] == "R":
                red_dq.append([i, j, 0])
            elif arr[j][i] == "B":
                blue_dq.append([i, j])

    while red_dq:
        red_x, red_y, red_count = red_dq.popleft()
        blue_x, blue_y = blue_dq.popleft()
        if red_count > 10:
            continue
        for i in range(4):
            red_nx, red_ny = red_x, red_y
            blue_nx, blue_ny = blue_x, blue_y
            temp_red, temp_blue = 0, 0

            while True:
                red_nx = red_x + dx[i]
                red_ny = red_y + dy[i]
                temp_red += 1

                blue_nx = blue_x + dx[i]
                blue_ny = blue_y + dy[i]
                temp_blue += 1
                if arr[red_ny][red_nx] == "O" and arr[blue_ny][blue_nx] != "O":
                    if red_count <= 10:
                        print(red_count)

                    else:
                        print(-1)
                    return
                if arr[red_ny][red_nx] != "O" and arr[blue_ny][blue_nx] == "O":
                    break

                if arr[red_ny][red_nx] == "#" and arr[blue_ny][blue_nx] != "#":
                    red_nx = red_x - dx[i]
                    red_ny = red_y - dy[i]
                    temp_red -= 1
                    continue
                if arr[red_ny][red_nx] != "#" and arr[blue_ny][blue_nx] == "#":
                    blue_nx = blue_x - dx[i]
                    blue_ny = blue_y - dy[i]
                    temp_blue -= 1
                    continue
                if arr[red_ny][red_nx] == "#" and arr[blue_ny][blue_nx] == "#":
                    break
                if arr[red_ny][red_nx] != "#" and arr[blue_ny][blue_nx] != "#":
                    continue
                # 끝까지 이동
            if arr[red_ny][red_nx] != "O" and arr[blue_ny][blue_nx] == "O":
                break

            if blue_ny == red_ny and blue_nx == red_nx:
                if temp_red > temp_blue:
                    red_nx -= dx[i]
                    red_ny -= dy[i]
                else:
                    blue_nx -= dx[i]
                    blue_ny -= dy[i]
                    # 겹칠 경우 처리

            red_dq.append([red_nx, red_ny, red_count + 1])
            blue_dq.append([blue_nx, blue_ny])
    print(-1)
solution()