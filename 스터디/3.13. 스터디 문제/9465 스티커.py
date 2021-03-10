import sys

input = sys.stdin.readline

T = int(input())


def solution(n, arr, max_):
    for i in range(n):
        for j in range(2):
            if i == 0:
                max_[j][i] = arr[j][i]
            elif i == 1:
                if j == 0:
                    max_[j][i] = arr[j][i] + max_[j + 1][i - 1]
                else:
                    max_[j][i] = arr[j][i] + max_[j - 1][i - 1]
            else:
                if j == 0:
                    max_[j][i] = arr[j][i] + max(max_[j + 1][i - 1], max_[j + 1][i - 2])
                else:
                    max_[j][i] = arr[j][i] + max(max_[j - 1][i - 1], max_[j - 1][i - 2])
    print(max(max_[0][n-1], max_[1][n-1]))


for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split(" "))) for _ in range(2)]
    max_ = [[0 for _ in range(n)] for _ in range(2)]
    solution(n, arr, max_)
