
m = int(input())
arr1 = sorted(list(map(int, input().split(" "))))
n = int(input())
arr2 = list(map(int, input().split(" ")))
ans = 0
def solution():

    for i in arr2:
        print(binary_search(arr1, i, 0, len(arr1)-1), end=" ")


def binary_search(arr1, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return 0

    if arr1[mid] == target:
        return 1
    elif arr1[mid] > target:
        return binary_search(arr1, target, start, mid-1)
    elif arr1[mid] < target:
        return binary_search(arr1, target, mid+1, end)
solution()