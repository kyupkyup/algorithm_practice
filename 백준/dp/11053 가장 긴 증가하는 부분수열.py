N = int(input())
arr = list(map(int, input().split(" ")))

def solution():
    ans = [1] * N

    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                ans[i] = max(ans[i], ans[j]+1)

    print(max(ans))

solution()