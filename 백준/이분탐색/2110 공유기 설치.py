
# 거리를 탐색하는 것
# C 개 만큼 선택했을 때, 최소 거리
# n 개 중 C 개 선택했을 때,

n, c = map(int, input().split(" "))
houses = []
for i in range(n):
    houses.append(int(input()))

def solution():
    houses.sort()
    start, end = 1, houses[-1] - houses[0]

    # 단위 거리가 1 ~ 8 까지 있고, 단위 거리 대로 공유기를 설치했을 때 맞아떨어지는 개수가 공유기 개수일 경우
    return binary_search(houses, start, end)

def binary_search(houses, start, end):
    # 단위 거리를 이분 탐색
    # 함수는 end값
    mid = (start + end) // 2
    count = find_house(mid, houses)
    if start > end:
        return mid

    if count < c:
        # 카운트가 C보다 적으면 단위거리가 너무 넓다는 뜻
        return binary_search(houses, start, mid-1)
    elif count >= c:
        # 카운트가 c보다 크거나 같으면 단위거리가 너무 좁다는 뜻 = 단위거리를 넓혀야 한다. 최대값에 가까워져야 한다.
        return binary_search(houses, mid+1,  end)


def find_house(gap, houses):
    start = houses[0]
    count = 1
    for i in range(1, len(houses)):
        if start + gap <= houses[i]:
            count += 1
            start = houses[i]
    return count


print(solution())