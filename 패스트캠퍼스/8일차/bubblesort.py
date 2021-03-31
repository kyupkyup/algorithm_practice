def bubble_sort(x):
    # 인접한 두 원소를 검사하여 정렬하고, 마지막 원소를 제외하고
    length = len(x) - 1
    for i in range(length):
        swapped = False
        for j in range(length - i):
            if x[j] > x[j + 1]:
                swapped = True
                x[j], x[j + 1] = x[j + 1], x[j]
        if not swapped:
            break
    return x


print(bubble_sort([4, 3, 2, 1]))

