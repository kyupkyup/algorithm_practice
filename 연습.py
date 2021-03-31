def bubble_sort(x):
    length = len(x) - 1
    for i in range(length):
        swapped = False

        for j in range(length - i):
            if x[j + 1] < x[j]:
                x[j], x[j + 1] = x[j + 1], x[j]
                swapped = True
        if not swapped:
            break
    return x


print(bubble_sort([1, 2, 3, -1, -2, -3]))


def insertion_sort(x):
    length = len(x)
    for i in range(1, length):
        j = i - 1
        key = x[i]
        while x[j] > key and j >= 0:
            x[j + 1] = x[j]
            j = j - 1
        x[j + 1] = key
    return x


print(insertion_sort([1, 2, 3, -1, -2, -3]))


def bubble_sort(x):
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
