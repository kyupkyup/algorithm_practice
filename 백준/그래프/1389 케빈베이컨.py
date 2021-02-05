N, M = map(int, input().split(" "))


arr = [[int(1e9)] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            arr[i][j] = 0
for _ in range(M):
    a, b = map(int, input().split(" "))
    arr[a][b] = 1
    arr[b][a] = 1

def solution():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
    ans = 1000000000
    answer = 0
    for i in range(1, N+1):
        if sum(arr[i]) - int(1e9) < ans:
            ans = sum(arr[i]) - int(1e9)
            answer = i

    print(answer)

solution()
