def bubblesort(x):
    # 
    for i in range(len(x) - 1):
        swapped = False
        for j in range(len(x) - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                swapped = True
        if not swapped:
            return x

    return x


print(bubblesort([1, 4, 6, 789, 3, 3, 6, 2, 45, 1]))


def insertionsort(x):
    for i in range(1, len(x)):
        j = i - 1
        key = x[i]

        while key < x[j] and j >= 0:
            x[j + 1] = x[j]
            j = j - 1
        x[j + 1] = key
    return x


x = [1, 4, 6, 789, 3, 3, 6, 2, 45, 1]
print(insertionsort(x))


def selectionsort(x):
    length = len(x)
    for i in range(length):
        min_index = i
        for j in range(i, length):
            if x[min_index] > x[j]:
                min_index = j
        x[i], x[min_index] = x[min_index], x[i]
    return x


x = [1, 4, 6, 789, 3, 3, 6, 2, 45, 1]
print(selectionsort(x))


def merge_sort(x, low, high, arr):
    if low >= high:
        return arr
    mid = (low + high) // 2
    merge_sort(x, low, mid, arr)
    merge_sort(x, mid + 1, high, arr)

    # 분할
    # 정복
    i, j = low, mid + 1
    for k in range(low, high + 1):
        if i > mid:
            arr[k] = x[j]
            j += 1
        elif j > high:
            arr[k] = x[i]
            i += 1
        elif i <= mid and j <= high:
            if x[i] <= x[j]:
                arr[k] = x[i]
                i += 1
            elif x[i] > x[j]:
                arr[k] = x[j]
                j += 1


    x[low:high + 1] = arr[low:high + 1]
    return arr
x = [1, 4, 6, 789, 3, 3, 6, 2, 45, 1]
print(merge_sort(x, 0, len(x)-1, [0]*len(x)))

def quicksort(x):
    if len(x) < 2:
        return x

    pivot = len(x) // 2
    l_arr = []
    r_arr = []
    for i in range(len(x)):
        if x[i] >= x[pivot] and i != pivot:
            r_arr.append(x[i])
        elif x[i] < x[pivot] and i != pivot:
            l_arr.append(x[i])

    return quicksort(l_arr) + [x[pivot]] + quicksort(r_arr)


x = [1, 4, 6, 789, 3, 3, 6, 2, 45, 1]
print(quicksort(x))

def quicksort_by_1(x, start, end):
    if start >= end:
        return

    pivot = (start+end) // 2
    f_start = start
    f_end = end

    while start <= end:
        while x[pivot] > x[start]:
            start += 1

        while x[pivot] < x[end]:
            end -= 1

        if start <= end:
            x[start], x[end] = x[end], x[start]
            start += 1
            end -= 1

    quicksort_by_1(x, f_start, start-1)
    quicksort_by_1(x, start, f_end)
    return x
x = [1, 4, 6, 789, 3, 3, 6, 2, 45, 1]
print(quicksort_by_1(x, 0 , len(x)-1))

