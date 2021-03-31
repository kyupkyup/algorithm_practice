def merge_sort(x, low, high, arr):
    if low >= high:  # 길이가 1이라면 혹은 길이가 0일수도있음
        return

    mid = (low + high )// 2

    merge_sort(x, low, mid, arr)
    merge_sort(x, mid + 1, high, arr)

    # 합쳐주는 방법
    i, j = low, mid + 1
    # low, mid+1 은 합병하는 내용인데 index 를 벗어나버릴 수도 있음 이걸 처리해줘야함
    for k in range(low, high + 1):
        if i > mid:
            arr[k] = x[j]
            j += 1
        elif j > high:
            arr[k] = x[i]
            i += 1
        elif i <= mid and j <= high:
            if x[i] > x[j]:
                arr[k] = x[j]
                j += 1
            else:
                arr[k] = x[i]
                i += 1

    x[low:high + 1] = arr[low:high + 1]
    return arr

x = [3, 5, 321, 3, 6, 23, 1, 223]
print(merge_sort(x, 0, len(x) - 1, [0] * len(x)))

