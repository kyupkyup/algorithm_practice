

N = int(input())
k = int(input())


def solution():
    left = 1
    right = N * N
    mid = (left + right) // 2
    return binary_search(mid, left, right)


def binary_search(mid, left, right):
    if left > right:
        return left

    mid = (left + right) // 2
    cal = calFunc(mid)


    if cal >= k : # cal 은 mid 보다 작은 수의 개수가 몇개인지를 보여주므로
        # cal 보다 k 가 크면 mid가 더 작아져야함
        return binary_search(mid, left, mid-1)
    elif cal < k:
        return binary_search(mid, mid + 1, right)


def calFunc(mid):
    sum = 0
    for i in range(1, N+1):
        if mid // i < N:
            sum += mid//i
        else:
            sum += N
    return sum

print(solution())