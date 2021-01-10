

# 이분탐색으로 가용 예산 최대값을 구하는 것

n = int(input())
budgets = list(map(int, input().split(" ")))
max_budget = int(input())

def solution():
    # 이분탐색을 통해 min 부터 max 사이의 값을 찾아서 max_budget에 가장 가까운 값을찾으면됨.
    start = 1
    end = max(budgets)
    return binary_search(start, end)

def binary_search(start, end):
    mid = (start + end) // 2
    ans = count_budget(mid)
    # mid 값을 함수에 넣어서 budges를 계산해보고 max_budget 보다 작다면 위로, 크다면 아래로
    if start > end:
        return mid
    if ans == max_budget:
        return mid
    elif ans > max_budget:
        return binary_search(start, mid-1)
    else:
        return binary_search(mid+1, end)

def count_budget(mid):
    budget = 0
    for i in budgets:
        if i >= mid:
            budget += mid
        elif i < mid:
            budget += i
    return budget

print(solution())