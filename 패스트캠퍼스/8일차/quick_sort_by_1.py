
def quick_sort(x, start, end):

    if start > end:
        return

    pivot = (start + end) // 2
    first_start = start
    first_end = end
    while start < end:
        while x[start] < x[pivot]: # 왼쪽 값 -> 더 큰 값있을경우 스왑
            start += 1
            if start >= end:
                break
        while x[end] > x[pivot]: # 오른쪽 값 -> 더 작은 값 스왑
            end -= 1
            if start >= end:
                break

        if start < end:
            x[start], x[end] = x[end], x[start]
            start += 1
            end -= 1

    quick_sort(x, first_start, start-1)
    quick_sort(x, end+1, first_end)
    return x

x = [9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9]
print(quick_sort(x, 0, len(x)-1))