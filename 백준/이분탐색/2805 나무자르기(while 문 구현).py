

# target 은 M
# height를 계속 바꿔가면서 M을 만들수 있는지 계속 탐색
# 1 ~ 나무의 최대값 까지 탐색

n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

def solution():
    print(binary_search(m, 1, max(arr)))


def binary_search(target, start, end):
    # 나무를 잘른 합이 m 보다 크면 높이를 늘여야하고, m보다 작으면 높이를 줄여야함
    while start <= end:
        mid = (start + end) // 2
        cut = cutting(mid)  # 커팅한 나무 길이

        if cut < target:
            end = mid - 1
        else:
            start =mid + 1

    return end




def cutting(height):
    sum = 0
    for i in arr:
        if i >= height:
            sum += i - height
    return sum

solution()