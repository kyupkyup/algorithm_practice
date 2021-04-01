def quick_sort(x, start, end):
    if start >= end:
        return

    pivot = (start + end) // 2
    first_start = start
    first_end = end
    while start <= end:
        while x[start] < x[pivot]:  # 왼쪽 값 -> 더 큰 값있을경우 스왑
            start += 1

        while x[end] > x[pivot]:  # 오른쪽 값 -> 더 작은 값 스왑
            end -= 1

        if start <= end:
            x[start], x[end] = x[end], x[start]
            start += 1
            end -= 1

    quick_sort(x, first_start, start - 1)
    quick_sort(x, start, first_end)
    return x


x = [3, 5, 321, 3, 6, 23, 1, 223,321]
x2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(quick_sort(x, 0, len(x) - 1))
print(quick_sort(x2, 0, len(x2) - 1))
