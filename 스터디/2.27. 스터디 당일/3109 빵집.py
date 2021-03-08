import sys
input= sys.stdin.readline

R, C = map(int, input().split(" "))
arr = [list(input().rstrip()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
dx = [1, 1, 1]
dy = [-1, 0, 1]
count = 0
check= False
def solution():
    global check
    # 원웅이빵집 완전탐색
    for i in range(R):
        dfs(0, i)
        check = False
    print(count)

def dfs(i, j):
    global count, check

    if i == R-1 and not check:
        check = True
        count += 1
        return

    for k in range(3):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < C and 0 <= ny < R:
            if not visited[ny][nx] and arr[ny][nx] != "x" and not check:
                visited[ny][nx] = True
                dfs(nx, ny)

solution()