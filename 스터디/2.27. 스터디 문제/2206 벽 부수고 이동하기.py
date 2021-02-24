import  sys
from _collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(" "))
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution():
    global arr, N, M, dx, dy

    dq = deque([[[0, 0], 0, 1]])
    visited[0][0][0] = True

    while dq:
        road, count, move = dq.popleft()
        if road[0] == M-1 and road[1] == N-1:
            print(move)
            return


        for i in range(4):
            temp_count = count
            nx = road[0] + dx[i]
            ny = road[1] + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if count > 0 and arr[ny][nx] == 1:
                    continue
                if visited[count][ny][nx]:
                    continue
                else:
                    visited[count][ny][nx] = True
                if arr[ny][nx] == 1:
                    temp_count += 1
                dq.append([[nx, ny], temp_count, move+1])

    print(-1)


solution()