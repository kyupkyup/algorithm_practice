from _collections import deque

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]


def solution():
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    y_length = len(maps)
    x_length = len(maps[0])
    visited = [[False for _ in range(x_length)] for _ in range(y_length)]
    dq = deque([])
    dq.append([0, 0, 1])

    while dq:
        x, y, count = dq.popleft()

        if x == x_length - 1 and y == y_length - 1:
            return count

        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < x_length and 0 <= ny < y_length:
                    if maps[ny][nx] == 1 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        dq.append([nx, ny, count + 1])
    return -1


print(solution())
