

n, m = map(int,input().split(" "))
lessons = list(map(int, input().split(" ")))


def solution():
    start = max(lessons)
    end = sum(lessons)

    return binary_search(start, end)

def binary_search(start, end):
    mid = (start + end) // 2
    count = find_blueray(mid)

    if start > end:
        return start

    if count > m:
        return binary_search(mid+1, end)
    else:
        return binary_search(start, mid-1)


def find_blueray(mid):
    start = 0
    count = 0
    for i in range(len(lessons)):
        if start + lessons[i] > mid:
            # 단위 크기와 같으면
            count += 1
            start = 0
        start = start + lessons[i]
    if start != 0:
        count += 1
    return count

print(solution())