# import sys
# sys.setrecursionlimit(15000)
# input = sys.stdin.readline
#
# N, M = map(int, input().split(" "))
# arr = [list(map(int, input().split(" "))) for _ in range(N)]
# dx = [-1, 1, 0, 0, -1, -1, 1, 1]
# dy = [0, 0, -1, 1, -1, 1, -1, 1]
# ans_tmp = 0
# ans = 0
# visited = [[False for _ in range(M)] for _ in range(N)]
#
#
# def solution():
#     global ans, visited, ans_tmp, N, M, arr
#
#     for i in range(M):
#         for j in range(N):
#             visited = [[False for _ in range(M)] for _ in range(N)]
#             count = 0
#             ans_tmp = 100
#             visited[j][i] = True
#             dfs(i, j, count)
#             ans = max(ans, ans_tmp)
#     print(ans)
#
# def dfs(k, j, count):
#     global arr, dx, dy, ans_tmp, N, M, visited
#     if arr[j][k] == 1:
#         ans_tmp = min(ans_tmp, count)
#         return
#
#     for i in range(8):
#         nx = k + dx[i]
#         ny = j + dy[i]
#         if 0 <= nx < M and 0 <= ny < N:
#             if arr[ny][nx] == 1:
#                 count += 1
#                 ans_tmp = min(ans_tmp, count)
#                 continue
#             else:
#                 if visited[ny][nx]:
#                     continue
#                 if count > ans_tmp:
#                     return
#                 else:
#                     visited[ny][nx] = True
#                     dfs(nx, ny, count + 1)
#     return
#
#
# solution()
