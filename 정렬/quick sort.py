
def partition(quick_list, start, end):
    # 피벗 기준으로 더 작은 값들을 왼쪽으로 보내고,
    # 큰 값은 오른쪽으로
    pivot = quick_list[start]
    left= start + 1
    right = end

    done = False

    while not done:
        while left <= right and quick_list[left] <= pivot:
            left += 1

        while left <= right and quick_list[right] > pivot:
            right -= 1

        if left > right:
            done= True
        else:
            quick_list[left], quick_list[right] = quick_list[right], quick_list[left]
        # left 와 right에서 한칸씩 안 쪽으로 온다.
        #  quick_list[left] 값이 pivot 보다 작으면 그대로 두고 left 포인터만 이동한다. 크다면 left 값 고정 해 두고
        # right 값을 마찬가지로 옮겨준다. right에서 pivot 보다 작은 값을 찾았다면 그 값과 left 값을 바꾸어준다.
    quick_list[start], quick_list[right] = quick_list[right], quick_list[start]
    return right

def quick(list1, start, end):
        if  start < end:
            pivot = partition(list1, start, end)
            quick(list1, start, pivot - 1)
            quick(list1, pivot + 1, end)
        return list1

def solution():
    seq= [3,4,5,2,41,56,56,4576]
    return quick(seq, 0, len(seq)-1)

print(solution())
