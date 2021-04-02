def solution(array, target_value):
    array.sort()
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] > target_value:
            left = mid + 1
        elif array[mid] < target_value:
            right = mid - 1
        else:
            return mid

    return -1

print(solution([1,2,3,4,5,6,7,8,2,3,4,10], 4))