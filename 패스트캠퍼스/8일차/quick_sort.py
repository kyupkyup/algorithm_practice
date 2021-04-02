

def quick_sort(x):
    if len(x) < 2:
        return x
    pivot = len(x) // 2

    arr1 = []
    arr2 = []

    for i in range(len(x)):
        if x[i] > x[pivot] and i != pivot:
            arr2.append(x[i])
        elif x[i] <= x[pivot] and i != pivot:
            arr1.append(x[i])

    return quick_sort(arr1) + [x[pivot]] + quick_sort(arr2)

print(quick_sort([3, 5, 321, 3, 6, 23, 1, 223]))


def quick_sort2(x, left, right):
    if left >= right:
        return []

    pivot_value = x[(left + right) // 2]
    arr_left = []
    arr_right = []

    for i in range(left, right+1):
        if x[i] < pivot_value:
            arr_left.append(x[i])
        elif x[i] >= pivot_value:
            arr_right.append(x[i])

    return quick_sort2(arr_left, 0, len(arr_left) - 2) + [pivot_value] + quick_sort2(arr_right, 1, len(arr_right) - 1)

x = [3, 5, 321, 3, 6, 23, 1, 223]
print(quick_sort2(x, 0, len(x)-1))
