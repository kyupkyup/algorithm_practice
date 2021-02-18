from collections import deque
import sys

def solution(N, arr):
    arr.sort()

    for i in range(1, N):
        if arr[i-1] == arr[i][0:len(arr[i-1])]:
            print("NO")
            return
    print("YES")

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = [sys.stdin.readline().strip() for _ in range(N)]
    solution(N, arr)

# def solution(N, arr):
#     global visited
#     dq = deque([])
#
#     for i in range(1, 11):
#         dq.append(arr[0][:i])
#         while dq:
#             temp = dq.popleft()
#             visited.append(temp)
#             check = False
#             count = 0
#             for j in range(N):
#                 if arr[j] == temp:
#                     check = True
#                 now = arr[j][:i]
#                 if now != temp:
#                     if now not in visited and now not in dq:
#                         dq.append(now)
#
#                 else:
#                     count += 1
#                     if check and count >= 2:
#                         print("NO")
#                         return
#     print("YES")
