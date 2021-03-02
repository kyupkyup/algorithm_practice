S = "4 5 6 - 7 +"
def solution(S):
    # write your code in Python 3.6
    arr = S.split(" ")
    stack = []
    for i in arr:
        if i == "POP":
            if stack:
                stack.pop()
            else:
                return -1
            if not stack:
                return -1
        elif i == "DUP":
            stack.append(stack[-1])
        elif i == "+":
            if stack:
                a = int(stack.pop())
            else:
                return -1
            if stack:
                b = int(stack.pop())
            else:
                return -1
            if a+b <= 1048575:
                stack.append(a+b)
            else:
                return -1
        elif i == "-":
            if stack:
                a = int(stack.pop())
            else:
                return -1
            if stack:
                b = int(stack.pop())
            else:
                return -1
            if a-b < 0:
                return -1
            else:
                stack.append(a-b)

        else:
            stack.append(i)
    return stack[-1]
print(solution(S))