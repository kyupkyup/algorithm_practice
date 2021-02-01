from collections import deque
arr = list(input())

def solution():
    dq = deque(["("])
    count = 0
    for i in range(1, len(arr)):
        if arr[i] == ")" and arr[i-1] == "(":
            dq.popleft()
            count += len(dq)
        elif arr[i] == "(":
            dq.append("(")
        elif arr[i] == ")":
            count += 1
            dq.popleft()
    print(count)
solution()