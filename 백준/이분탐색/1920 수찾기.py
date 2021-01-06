
N = int(input())
A = sorted(list(map(int, input().split(" "))))
M = int(input())
arr = list(map(int, input().split(" ")))

def solution():

    # arr 순회하면서 각각을 타겟으로 하고
    # 이분탐색으로 A 에서 타겟이 있는 지 검색
    # 순서가 있으므로 arr을 먼저 for문
    for i in arr:
        print(binary_search(A, i, 0, len(A)-1))



def binary_search(seq, target,  start, end):
    mid = (start + end)//2
    if target == seq[mid]:
        return 1
    elif start == end:
        return 0
    elif target <= seq[mid]:
        return binary_search(seq, target, start, mid)
    elif target > seq[mid]:
        return binary_search(seq, target, mid+1, end)


solution()