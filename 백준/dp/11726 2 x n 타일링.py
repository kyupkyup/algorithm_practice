
n = int(input())
ans = [0] * (n+1)


def solution():
    global n, ans
    fibo(n)

    print(ans[n] % 10007)
    return

def fibo(n):

    if ans[n] > 0:
        return ans[n]
    if n == 1:
        ans[1] = 1
        return 1
    elif n == 2:
        ans[2] = 2
        return 2

    else:
        ans[n] = fibo(n-1) + fibo(n-2)
        return ans[n]
solution()