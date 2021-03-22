import re
p1 = re.compile('[a-z]+')
p2 = re.compile('[A-Z]+')
p3 = re.compile('[0-9]+')
p4 = re.compile('[~!@#$%^&*]+')

def solution(inp_str):
    ans =[]
    count = 0
    if  len(inp_str) < 8 and len(inp_str)  > 15:
        ans.append(1)
    m1 = p1.match(inp_str)
    m2 = p2.match(inp_str)
    m3 = p3.match(inp_str)
    m4 = p4.match(inp_str)
    if m1 == None:
        count += 1
    elif m2 == None:
        count += 1
    elif m3 == None:
        count += 1
    elif m4 == None:
        count += 1
    if 3> count > 0:
        ans.append

    return answer