
def solution(n, times):
    left, right = 0, 1000000000

    while left <= right:
        mid = (left + right) // 2

        sum = 0
        for i in times:
            sum += mid // i
        if sum == n:
            right -= 1
            continue

        elif sum < n:
            left = mid + 1
        elif sum > n:
            right = mid -1

    return left
print(solution(6, [7,10]))

