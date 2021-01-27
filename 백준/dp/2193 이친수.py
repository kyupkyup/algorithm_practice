
N = int(input())
ans = [0] * (N+1)


def solution():

    fibo(N)
    print(ans[N])

def fibo(n):

    if ans[n] > 0:
        return ans[n]
    elif n == 1:
        ans[n] = 1
        return 1
    elif n == 2:
        ans[n] = 1
        return 1
    else:
        ans[n] = fibo(n-2) + fibo(n-1)
        return ans[n]

solution()