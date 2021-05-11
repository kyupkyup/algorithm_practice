from _collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
kx = [-1, 1, -1, 1]
ky = [-1, 1, 1, -1]



def solution():
    x1, y1, x2, y2 = 0,0,14,17

    dq1 = deque([[x1, y1, 0]])
    dq2 = deque([[x2, y1, 0]])
    visited1 = set()
    visited2 = set()

    while dq1 and dq2:
        x1, y1, count1 = dq1.popleft()
        x2, y2, count2 = dq2.popleft()
        if x1 == x2 and y1 == y2:
            return min(count2, count1)
        else:
            for i in range(4):
                nx = x1 + dx[i]
                ny = y1 + dy[i]
                mx = x2 + kx[i]
                my = y2 + ky[i]
                if -100000 <= nx <= 100000 and  -100000 <= ny <= 100000:
                    if (nx, ny )not in visited1:
                        dq1.append([nx,ny,count1+1])
                        visited1.add((nx,ny))
                if -100000 <= mx <= 100000 and -100000 <= my <= 100000:
                    if (mx, my) not in visited2:
                        dq2.append([mx, my, count2+ 1])
                        visited2.add((mx, my))

print(solution())