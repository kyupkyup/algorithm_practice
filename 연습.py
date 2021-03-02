
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    str1 = bin(N)
    count = 0
    ans = 0
    for i in str1[2:]:
        if i == "0":
            count += 1
        else:
            ans = max(count, ans)
            count = 0

    if str1[-1] == "0":
        ans = 0
    print(ans)
    return ans
solution(15)