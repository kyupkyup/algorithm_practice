##
import sys
N = int(input())
arr = list(map(int, input().split(" ")))
ans_real = 1000000000000
sys.setrecursionlimit(100000)
ans_list = []
def solution():
    # 인덱스  양 끝에서 안쪽으로 들어옴
    left = 0
    right = N-1
    return binary_search(left, right)


def binary_search(left, right):
    global ans_real, ans_list

    if left >= right:
        return
    ans_temp = arr[left] + arr[right]

    if ans_real > abs(ans_temp):
        ans_real = abs(ans_temp)
        ans_list = [arr[left], arr[right]]

    if ans_temp > 0:
        return binary_search(left, right-1)
    else:
        return binary_search(left+1, right)



solution()
print("{} {}".format(ans_list[0], ans_list[1]))