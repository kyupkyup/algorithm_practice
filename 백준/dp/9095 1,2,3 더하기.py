T = int(input())
count = 0

def solution():
    global count
    for _ in range(T):
        n = int(input())
        dp(0, n)
        print(count)
        count = 0

def dp(i, n):
    # 여기에서 i가 n과 같으면 count ++ return
    # 더 크면 그냥 리턴
    # 작으면 1,2,3 각 더하는 것으로 재귀
    global count
    if i == n:
        count += 1
        return
    elif i > n:
        return
    else:
        dp(i+1, n)
        dp(i+2, n)
        dp(i+3, n)
        return


solution()