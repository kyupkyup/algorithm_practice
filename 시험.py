def recursive(x):
    if x == 1:
        return 1
    else:
        return x * recursive(x - 1)


print(recursive(4))


def merge_sort(x, left, right, arr):
    if left >= right:
        return x
    mid = (left + right) // 2

    merge_sort(x, left, mid, arr)
    merge_sort(x, mid + 1, right, arr)

    i, j = left, mid + 1
    for k in range(left, right + 1):
        if i > mid:
            arr[k] = x[j]
            j += 1
        elif j > right:
            arr[k] = x[i]
            i += 1
        elif i <= mid and j <= right:
            if x[i] > x[j]:
                arr[k] = x[j]
                j += 1
            else:
                arr[k] = x[i]
                i += 1
    x[left:right + 1] = arr[left:right + 1]
    return x

x = [1, 3, 9, 56, 4, 3, 5, 7, 2, 6, 89, 9, 2, 1, 4,20,45,12,1,2,3,9,8,7,1,5,4,6,7,8,4,3,23,5,5,]
print(merge_sort(x, 0, len(x) - 1, [0] * len(x)))
