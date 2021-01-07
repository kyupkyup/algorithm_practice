

# 최대 랜선의 길이를 탐색
# 가져온 랜선의 최대 길이를 구해서
# 그 사이에서 이분탐색

k, n = map(int, input().split(" "))
arr = []
for i in range(k):
    arr.append(int(input()))

def solution():
    # 나누기를 해서 몫들을 모두 합침.
    print(binary_search(n, 1, max(arr)))



def binary_search(target, start, end):
    mid = (start + end) // 2
    if start > end:
        return end

    if divide(mid) >= target:
        # 너무 작게 자른것, 더 크게 잘라야 함
        return binary_search(target, mid+1, end)
    else:
        return binary_search(target, start, mid-1)

def divide(value):
    sum = 0
    for i in arr:
        if i >= value:
            sum += i // value
    return sum


solution()