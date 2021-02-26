import sys
from _collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(N)]
my_dict = defaultdict(int)
start = [0,0]

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

for i in range(N):
    for j in range(N):
        if 6 >= arr[j][i] > 0:
            my_dict[arr[j][i]] += 1
        if arr[j][i] == 9:
            start[0], start[1] = i, j
            arr[j][i] = 0


def solution():
    global start, N, arr, my_dict, dx, dy
    shark = 2
    count = 0

    dq = deque([])
    dq.append([start, 0])

    if check(shark) == 0:
        print(0)
        return

    while dq:
        point, timer = dq.popleft()
        can_eat = []
        for i in range(4):
            nx = point[0] + dx[i]
            ny = point[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if 0 < arr[ny][nx] < shark:
                    count += 1
                    if count == shark:
                        shark += 1
                        count = 0
                    my_dict[arr[ny][nx]] -= 1
                    if check(shark) == 0:
                        print(timer+1)
                        return

                    arr[ny][nx] = 0
                    dq.clear()
                    dq.append([[nx, ny], timer+1])
                    break
                elif arr[ny][nx] == shark or arr[ny][nx] == 0:
                    dq.append([[nx, ny], timer+1])
                elif arr[ny][nx] > shark:
                    continue

    print(timer)

def check(shark):
    global my_dict
    count = 0
    for i in range(shark):
        if my_dict[i] != 0:
            count += my_dict[i]
    if count == 0:
        return 0
    elif count == 1:
        return 1
    else:
        return 2




solution()