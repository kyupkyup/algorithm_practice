import sys
S = sys.stdin.readline().strip()

def solution():
    global S
    S_length = len(S)
    ans = 0

    for i in range(S_length):
        for j in range(i+1, S_length):
            if S[i] == S[j]:
                temp = 1
                ans = max(ans, temp)

                p1, p2 = i+1, j+1
                while p1 < S_length and p2 < S_length:
                    if S[p1] == S[p2]:
                        temp += 1
                        ans = max(ans, temp)
                    else:
                        break

                    p1 += 1
                    p2 += 1

    print(ans)#

solution()