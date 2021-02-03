from _collections import deque

def solution(M, N, K, arr):
    dq = deque([])
    count = 0
    for i in range(M):
        for j in range(N):
            if arr[j][i] == 1:
                dq.append([i, j])
                count += 1
            while dq:
                temp = dq.popleft()

                right = temp[0] + 1
                left = temp[0] - 1
                up = temp[1] - 1
                down = temp[1] + 1

                if right < M:
                    if arr[temp[1]][right] == 1:
                        dq.append([right, temp[1]])
                        arr[temp[1]][right] = 0

                if down < N:
                    if arr[down][temp[0]] == 1:
                        dq.append([temp[0], down])
                        arr[down][temp[0]] = 0

                if left >= 0:
                    if arr[temp[1]][left] == 1:
                        dq.append([left, temp[1]])
                        arr[temp[1]][left] = 0

                if up >= 0:
                    if arr[up][temp[0]] == 1:
                        dq.append([temp[0], up])
                        arr[up][temp[0]] = 0

    print(count)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split(" "))
    arr = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split(" "))
        arr[y][x] = 1
    solution(M, N, K, arr)




