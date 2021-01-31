from collections import deque

N, K = map(int, input().split(" "))
memo = [False for _ in range(100001)]


def solution():

    dq = deque([[N, 0]])

    while dq:
        temp, count = dq.popleft()
        memo[temp] = True

        if temp == K:
            print(count)
            return
        else:
            if temp * 2 < 100001:
                if not memo[temp*2]:
                    dq.append([temp * 2, count + 1])
            if temp - 1 >= 0:
                if not memo[temp-1]:
                    dq.append([temp - 1, count + 1])
            if temp + 1 < 100001:
                if not memo[temp+1]:
                    dq.append([temp + 1, count + 1])
    return


solution()