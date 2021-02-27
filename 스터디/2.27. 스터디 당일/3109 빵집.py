import sys
input= sys.stdin.readline

R, C = map(int, input().split(" "))
arr = [list(input().rstrip()) for _ in range(C)]
visited = [[False for _ in range(C)] for _ in range(R)]
dx = [-1, -1, -1]
dy = [-1, 0, 1]

def solution():

    # 원웅이빵집 완전탐색
    for i in range(C):
        dfs(R-1, C)


def dfs(i, j):

    if arr[j][i] == "x":
        return



    for k in range(3):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < R and 0 <= ny < C:
            dfs(nx, ny)




solution()