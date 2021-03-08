import sys, copy
from _collections import deque
input = sys.stdin.readline().rstrip()

s, t = input.split(" ")
operator = ["*", "+", "-", "/"]
check1, check0 = False, False
def solution():
    global check1, check0, s, t, operator
    if s == t:
        print(0)
        return
    ans = []
    dq = deque([])
    dq.append([s, ans])

    while dq:
        mid_value, ans = dq.popleft()
        if mid_value == "1":
            if not check1:
                check1 = True
            else:
                continue

        if mid_value == "0":
            if not check0:
                check0 = True
            else:
                continue

        int_va, int_t = int(mid_value), int(t)

        if int_va * int_va <= int(t) and int_va + int_va <= int(t):


            for i in range(4):
                temp_ans = copy.deepcopy(ans)
                temp_mid = mid_value
                temp_mid = int(eval(temp_mid + operator[i] + temp_mid))
                if temp_mid == int(t):
                    print(ans)
                    return
                temp_ans.append(operator[i])
                if temp_mid == 0:
                    continue
                dq.append([str(temp_mid), temp_ans])
    print(-1)








solution()