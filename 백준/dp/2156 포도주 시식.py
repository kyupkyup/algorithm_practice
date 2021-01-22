n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
ans = [0] * (n+1)

def solution():
    ans[1] = arr[1]
    if n > 1:
        ans[2] = arr[2] + arr[1]

    if n > 2:
        for i in range(3, n+1):
            ans[i] = max(arr[i] + arr[i-1] + ans[i-3], ans[i-1], arr[i] + ans[i-2])
    print(max(ans))

solution()
