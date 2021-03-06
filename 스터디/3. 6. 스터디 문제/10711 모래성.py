import sys
from _collections import deque
input = sys.stdin.readline

H, W = map(int, input().split(" "))

arr = [list(input()) for _ in range(H)]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def solution():

    pado = 0
    while True:
        check = False
        stack = []
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
                        check = True
                        stack.append([i, j])
        for i, j in stack:
            arr[j][i] = "."

        if not check:
            print(pado)
            return
        pado += 1

solution()