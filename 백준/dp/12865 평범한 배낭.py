N, K = map(int, input().split(" "))

arr_weight = [0] * N
arr_value = [0] * N
max_value = 0
for i in range(N):
    arr_weight[i], arr_value[i] = map(int, input().split(" "))

ans = [[0 for _ in range(K+1)] for _ in range(N+1)]

def solution():

    for current_pack in range(1, N+1):
        for current_weight in range(1,K+1):
            # 해당 무게보다 j 값이 작으면 이전 값 가져옴 만약 크면
            if arr_weight[current_pack-1] > current_weight:
                ans[current_pack][current_weight] = ans[current_pack-1][current_weight]
            else:
                ans[current_pack][current_weight] = max(ans[current_pack-1][current_weight], arr_value[current_pack-1] + ans[current_pack-1][current_weight-arr_weight[current_pack-1]])

    print(ans[N][K])


solution()