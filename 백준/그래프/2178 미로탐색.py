from collections import deque

n, m = map(int, input().split(" "))
arr = [list(map(int, list(input()))) for _ in range(n)]
count = 0


def solution():
    global count
    dq = deque([[[0, 0], 1]])

    while dq:
        temp, count = dq.popleft()


        if temp == [m - 1, n - 1]:
            print(count)
            break
        right = temp[0]+1
        left = temp[0]-1
        up = temp[1]-1
        down = temp[1]+1

        if right < m:
            if arr[temp[1]][right] == 1:
                dq.append([[right, temp[1]], count + 1])
                arr[temp[1]][right] = 0

        if down < n:
            if arr[down][temp[0]] == 1:
                dq.append([[temp[0], down], count + 1])
                arr[down][temp[0]] = 0

        if left >= 0:
            if arr[temp[1]][left] == 1:
                dq.append([[left, temp[1]], count + 1])
                arr[temp[1]][left] = 0

        if up >= 0:
            if arr[up][temp[0]] == 1:
                dq.append([[temp[0], up], count + 1])
                arr[up][temp[0]] = 0


solution()
