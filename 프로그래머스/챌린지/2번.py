

def solution(s):
    def cnt(s):
        count = 0
        dict1 = 0
        dict2 = 0
        dict3 = 0
        for i in range(len(s)):
            if s[i] == ")" and dict1 > 0:
                count += 1
                dict1 -= 1
            elif s[i] == "}" and dict2 > 0:
                count += 1
                dict2 -= 1
            elif s[i] == "]" and dict3 > 0:
                count += 1
                dict3 -= 1

            if s[i] == "(":
                dict1 += 1
            elif s[i] == "{":
                dict2 += 1
            elif s[i] == "[":
                dict3 += 1
        if count < 3:
            return False
        if dict1 != 0 or dict2 !=0 or dict3 != 0:
            return False
        return True
    answer = 0
    for i in range(len(s)):
        s += s[0]
        s = s[1:]
        if cnt(s):
            answer += 1
    return answer
print(solution("[](){}"))