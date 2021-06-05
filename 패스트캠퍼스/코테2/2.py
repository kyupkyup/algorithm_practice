
def solution(n):
    str1 = str(n)
    check = set()
    def recursive(str1):
        nonlocal check
        check.add(str1)
        if int(str1) == 1:
            return True
        ans = 0
        for i in str1:
            ans += int(i) ** 2
        str_ans = str(ans)
        if str_ans in check:
            return False
        return recursive(str_ans)
    return recursive(str1)

print(solution(4))