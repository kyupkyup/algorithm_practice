N = int(input())

arr = list(map(int, input().split(" ")))
arr.insert(0, -1000)
ans = [-1000] * (N+1)

def solution():
    global ans, arr, N
    for i in range(1, N+1):
        ans[i] = max(arr[i], arr[i] + ans[i-1])
    print(max(ans))


solution()