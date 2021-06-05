from _collections import deque
from random import *

def solution(depth, n, blocks):
    # depth, n 에서 시작해서 bfs 돌기
    dq = deque([[n, depth, blocks[depth][n]]])
    answer = 1000000000
    while dq:
        x, y, energy = dq.popleft()
        if y > 0:
            if x > 0:
                dq.append([x - 1, y - 1, energy + blocks[y - 1][x - 1]])
            if x < len(blocks[0]) - 1:
                dq.append([x + 1, y - 1, energy + blocks[y - 1][x + 1]])
            dq.append([x, y - 1, energy + blocks[y - 1][x]])

        elif y == 0:
            answer = min(answer, energy)

    return answer

arr = [[randint(1,1000) for _ in range(100)] for _ in range(100)]
print(arr)
print(solution(99, 99, arr))
