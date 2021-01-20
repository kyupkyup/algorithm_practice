N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split(" "))))

ans = [0 for i in range(N+1)]


def solution():

    # 뒤에서 부터 dp 시작 N - Tn 이 0 초과면 불가능
    #  for 문 n부터 0으로
    for i in range(N-1, -1, -1):
        if i + arr[i][0] > N:
            ans[i] = 0
        else:
            ans[i] = max(arr[i][1] + max(ans[i+arr[i][0]:]), ans[i+arr[i][0]])
            # 지금 i 값의 Tn 을 더한 p값과, 현재 나만의 값을 비교 더 큰 쪽
    print(max(ans))
solution()