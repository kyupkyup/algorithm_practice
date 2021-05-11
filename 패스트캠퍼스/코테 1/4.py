N = 4
K1 = 3
K2 = 8
W = [1, 5, 6, 3]
V = [5, 2, 14, 6]
arr_weight = [0] * N
arr_value = [0] *  N
max_value = 0


ans = [[[0 for _ in range(K1+1)] for _ in range(K2+1)] for _ in range(N+1)]

def solution():

    for i in range(1, N+1):
        for j in range(1,K1+1):
            for k in range(1, K2 + 1):
            # 해당 무게보다 j 값이 작으면 이전 값 가져옴 만약 크면
            if arr_weight[i-1] > j:
                ans[i][j] = ans[i-1][j]
            else:
                ans[i][j] = max(ans[i-1][j], arr_value[i-1] + ans[i-1][j-arr_weight[i-1]])

    print(ans[N][K])


solution()