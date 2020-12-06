def str_compression(s):
    count, last = 1, ""
    list_aux = []

    for i, c in enumerate(s): # (0, 글자) 튜플 형태로 저장
        if last == c:  # 현재 지정된 글자가 반복된다면
            count += 1 # 카운트 더해줌
        else:   # 새로운 글자가 나왔다면
            if i!= 0: # 현재 첫번째 글자를 가르키고 있는게 아니라면
                list_aux.append(str(count)) # 숫자 + 글자
            list_aux.append(c)
            count = 1 # 카운트 초기화 하고
            last = c # 새로운 글자 가 몇개인지 다시 세 줌
    list_aux.append(str(count))  # 마지막에 개수 세는 걸 해줘야되서 있어야함
    return "".join(list_aux) #문자열로 만들어주기

if __name__ == "__main__":
    result = str_compression("aaaaaabbbbbcccc")
    print(result)