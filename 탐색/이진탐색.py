

def binary_search(seq, target, low, high):
    if low > high:
        return None
    mid = (low + high) // 2

    if target == seq[mid]:
        return mid
    elif target< seq[mid]:
        return binary_search(seq, target, low, mid-1)
    else:
        return binary_search(seq, target, mid, high)


def partition(seq, start, end):
    pivot = seq[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and seq[left] <= pivot:
            left += 1
        while left <= right and seq[right] > pivot:
            right -= 1
        if left > right:
            done = True
        else:
            seq[left], seq[right] = seq[right], seq[left]
    seq[start], seq[right] = seq[right], seq[start]
    return right



def quick_sort(seq, start, end):
    if start < end:
        pivot = partition(seq, start, end)
        quick_sort(seq, start, pivot-1)
        quick_sort(seq, pivot+1, end)
    return seq
def solution():
    seq = [4,6,2,1,7,9,2,3,4,2]
    target = 7
    # 퀵정렬을  톻해 정렬을 하고, 이진 탐색 시작
    seq = quick_sort(seq, 0, len(seq)-1)
    print(seq)
    print(binary_search(seq, target, 0, len(seq)-1))



solution()






