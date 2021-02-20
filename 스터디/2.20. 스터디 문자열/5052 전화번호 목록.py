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
