def insertion_sort(x):
    for i in range(1, len(x)):
        j = i - 1
        key = x[i]
        while x[j] > key and j >= 0:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = key
    return x


print(insertion_sort([4, 3, 2, 1]))