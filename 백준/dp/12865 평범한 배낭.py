N, K = map(int, input().split(" "))

arr_weight = [0] * N
arr_value = [0] * N
max_value = 0
for i in range(N):
    arr_weight[i], arr_value[i] = map(int, input().split(" "))
