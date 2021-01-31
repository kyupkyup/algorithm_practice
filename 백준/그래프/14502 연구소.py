from collections import deque
from copy import deepcopy

N, M = map(int, input().split(" "))
arr = [list(map(int, input().split(" "))) for _ in range(N)]

def solution():
    count, ans = 0, -1
    dq = deque([])
    temp_arr = deepcopy(arr)
    
    for two_pointer_ver in range(N):
        for two_pointer_hori in range(M):
            if arr[two_pointer_ver][two_pointer_hori] == 2:
                dq.append([two_pointer_hori, two_pointer_ver])

    temp_dq = deepcopy(dq)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                for k in range(N):
                    for l in range(M):
                        if i == k and j == l:
                            continue
                        else:
                            if arr[k][l] == 0:
                                for m in range(N):
                                    for n in  range(M):
                                        if (k == m and l == n)  or (i == m and j == n): # 점이 같을 경우
                                            continue
                                        elif arr[m][n] == 0:
                                            temp_arr[i][j], temp_arr[k][l], temp_arr[m][n] = 1, 1, 1
                                        else:
                                            continue
                                    # bfs 실행
                                        while temp_dq:
                                            temp = temp_dq.popleft()

                                            right = temp[0] + 1
                                            left = temp[0] - 1
                                            up = temp[1] - 1
                                            down = temp[1] + 1

                                            if right < M:
                                                if temp_arr[temp[1]][right] == 0:
                                                    temp_dq.append([right, temp[1]])
                                                    temp_arr[temp[1]][right] = 2

                                            if down < N:
                                                if temp_arr[down][temp[0]] == 0:
                                                    temp_dq.append([temp[0], down])
                                                    temp_arr[down][temp[0]] = 2

                                            if left >= 0:
                                                if temp_arr[temp[1]][left] == 0:
                                                    temp_dq.append([left, temp[1]])
                                                    temp_arr[temp[1]][left] = 2

                                            if up >= 0:
                                                if temp_arr[up][temp[0]] == 0:
                                                    temp_dq.append([temp[0], up])
                                                    temp_arr[up][temp[0]] = 2

                                        for two_pointer_ver in range(N):
                                            for two_pointer_hori in range(M):
                                                if temp_arr[two_pointer_ver][two_pointer_hori] == 0:
                                                    count += 1

                                        ans = max(ans, count)
                                        count = 0
                                        temp_arr = deepcopy(arr)
                                        temp_dq = deepcopy(dq)
    print(ans)
solution()