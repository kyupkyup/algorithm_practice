def selection_sort(x):
    length = len(x)
    for i in range(length-1):
        index_min = i
        for j in range(i+1, length):
            if x[index_min] > x[j]:
                index_min = j

        x[i], x[index_min] = x[index_min], x[i]
    return x

print(selection_sort([4, 3, 2, 1]))