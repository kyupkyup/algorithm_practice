
n = 4
record=["1 a","1 b","1 abc","3 b","3 a","1 abcd","1 abc","1 aaa","1 a","1 z","1 q", "3 k", "3 q", "3 z", "3 m", "3 b"]
ans = [[] for i in range(n+1)]
answer = []

def solution(n, record):
    for i in range(1,n+1):
        for j in range(len(record)):
            if int(record[j][0]) == i:
                # 이미 5개가 꽉차있는경우
                # 똑같은 이름이 있는경우

                if record[j][2:] in ans[i]:
                    continue
                elif len(ans[i]) >= 5:
                    del ans[i][0]
                    ans[i].append(record[j][2:])

                else:
                    ans[i].append(record[j][2:])
    for i in ans:
        for j in i:
           answer.append(j)
    return answer

solution(n, record)