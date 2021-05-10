import heapq
from itertools import permutations
from copy import deepcopy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(board, r, c):
    answer = 1000000000
    a = set()
    for i in range(4):
        for j in range(4):
            if board[j][i] > 0:
                a.add(board[j][i])

    combination = list(permutations(a, len(a)))
    heap = []
    visited= set()
    for comb in combination:
        temp_board = deepcopy(board)
        sum_count = 0
        count = 0
        heapq.heappush(heap, [0, c, r])
        visited.add((c,r))
        for pick in comb:
            is_found = False
            while heap:
                count, x, y = heapq.heappop(heap)
                if temp_board[y][x] == pick:
                    if is_found:
                        sum_count += count +1
                        heap=[]
                        visited = set()
                        visited.add((x,y))
                        heapq.heappush(heap, [0, x, y])
                        temp_board[y][x] = 0
                        break
                    else:
                        temp_board[y][x] = 0
                        sum_count += count + 1
                        visited = set()
                        visited.add((x,y))
                        heap=[]
                        heapq.heappush(heap, [0, x, y])
                        is_found = True
                        continue
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < 4 and 0 <= ny < 4:
                        if (nx, ny) not in visited:
                            heapq.heappush(heap, [count + 1, nx, ny])
                for m in range(4):
                    nx, ny = x, y
                    while True:
                        nx = nx + dx[m]
                        ny = ny + dy[m]
                        if nx < 0:
                            nx += 1
                            break
                        elif nx > 3:
                            nx -= 1
                            break
                        elif ny < 0:
                            ny += 1
                            break
                        elif ny > 3:
                            ny -= 1
                            break
                        if temp_board[ny][nx] > 0:
                            break
                    if 0 <= nx < 4 and 0 <= ny < 4:
                        if (nx, ny) not in visited:
                            heapq.heappush(heap, [count + 1, nx, ny])
        answer = min(answer, sum_count)
    return answer

board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
r = 0
c = 1
print(solution(board, r, c))
