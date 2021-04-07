def solution(money):
    n = len(money)
    money.insert(0, 0)
    ans1 = [0] * (n + 1)
    ans2 = [0] * (n + 1)

    for i in range(1, n):
        if i == 1:
            ans1[i] = money[i]
        elif i == 2:
            ans1[i] = max(money[i], money[i - 1])
        else:
            ans1[i] = max(ans1[i - 1], money[i] + ans1[i - 2])

    for i in range(2, n + 1):

        if i == 2:
            ans2[i] = money[i]
        else:
            ans2[i] = max(ans2[i - 1], money[i] + ans2[i - 2])

    return max(ans1[n-1], ans2[n])

print(solution([1,2,3,6]))

