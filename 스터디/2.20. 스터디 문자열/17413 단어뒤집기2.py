S = input()
arr = []
temp = 0
check = False

def solution():
    global temp, check

    for i in range(len(S)):
        if S[i] == "<":
            arr.append(S[temp:i])
            check = True
            temp = i
        elif S[i] == ">":
            arr.append(S[temp:i+1])
            check = False
            temp = i + 1
        elif S[i] == " " and not check:
            arr.append(S[temp:i])
            arr.append(" ")
            temp = i + 1
    arr.append(S[temp:])

    for word in arr:
        if word and word[0] == "<":
            print(word, end="")
        elif word == " ":
            print(word, end="")
        else:
            for i in range(len(word)-1, -1, -1):
                print(word[i], end="")

solution()
