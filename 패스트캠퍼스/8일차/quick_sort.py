

def quick_sort(x):
    pivot = len(x)-1
    if len(x) == 0:
        return []
    arr1 = []
    arr2 = []

    for i in range(len(x)-1):
        if x[i] > x[pivot]:
            arr2.append(x[i])
        else:
            arr1.append(x[i])

    return quick_sort(arr1) + [x[pivot]] + quick_sort(arr2)
print(quick_sort([3, 5, 321, 3, 6, 23, 1, 223]))


