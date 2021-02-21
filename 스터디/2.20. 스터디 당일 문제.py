s = ")("

def solution(s):
    answer = []
    answer = recursive(s, answer)

    return answer

def recursive(s , answer):
    countRight1 = 1
    countRight2 = 0
    countBalance1 = 1
    countBalance2 = 0
    if s == "": # 1번
        return s


    for i in range(1, len(s)):
        if s[0] == "(":
            if s[i] == "(": # 처음나오는 균형잡힌 괄호 문자열
                countRight1 += 1 # 1 = ( 개수, 2 = ) 개수
            elif s[i] == ")":
                countRight2 += 1
            if countRight1 == countRight2:
                # 올바른 문자열로 만듬
                answer = s[:i+1]+ recursive(s[i+1:], answer) # 균형잡힌 문자열 확인
                return answer
        elif s[0] == ")":
            #균형
            if s[i] == ")":
                countBalance1 += 1
            elif s[i] == "(":
                countBalance2 += 1
            if countBalance1 == countBalance2:
                #균형잡힌 문자열

                answer = "(" + recursive(s[i+1:], answer) + ")" + convert(s[1:i])

                return answer

def convert(s):
    ans = ""
    for j in range(len(s)):
        if s[j] == "(":
            ans += ")"
            continue#
        elif s[j] == ")":
            ans += "("
            continue
    return ans
solution(s)