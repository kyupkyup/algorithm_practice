from collections import deque


def parsing(exp):
    operators = []
    numbers = []

    res = ""  # result
    q = deque([])
    opers = set("+-*/")

    for c in exp:
        if c not in opers:
            q.append(c)
            continue

        operators.append(c)
        while q:
            res += q.popleft()
        if res:
            numbers.append(int(res))
        res = ""

    while q:
        res += q.popleft()
    numbers.append(int(res))
    if exp[0] == "-":
        numbers[0] *= -1
        del operators[0]

    return (numbers, operators)


def solution():
    numbers, operators = parsing("-11-1-1-1")
    priority = {
        "*" : 2,
        "/" : 2,
        "-" : 1,
        "+" : 1
    }
    left_oper = 0
    right_oper = len(operators)-1

    left_num = 0
    right_num = len(operators)-1

    flag = False

    left_tmp = 0
    right_tmp = 0

    while left_num <= right_num:
        if flag:
            left_tmp = numbers[left_num]
            right_tmp = numbers[right_num]
            right_tmp -= 1
            left_tmp += 1
            continue

        if priority[left_oper] < priority[right_oper]:
            eval(numbers[right_tmp] + operators[right_oper] + right_tmp)


    # 우선순위
    # numbers.append(eval(str(numbers[left_num])+operators[left_oper]+str(numbers[left_num+1])))
    # numbers.append(eval(str(numbers[right_num])+operators[right_oper]+str(numbers[right_num-1])))
    print(numbers)

    # 3, 2, 5, 5, 7
    # * + - +









    return


solution()
