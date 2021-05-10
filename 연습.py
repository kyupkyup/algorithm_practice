
    def solution(sentence, keyword, skips):
        answer =""
        p1=0
        p2=0

        for skip in skips:
            for i in range(skip):
                if p1 >= len(sentence):
                    return answer
                answer += sentence[p1]
                if keyword[p2] == sentence[p1]:
                    p1+=1
                    break
                p1 += 1
            answer += keyword[p2]
            p2 = ((p2+1) % len(keyword))
        while p1 < len(sentence):
            answer += sentence[p1]
            p1 += 1
        return answer

sentence = "encrypt this sentence"
keyword = "something"
skips = [0,1,3,2,1,2,0,3,0,2,4,1,3]
print(solution(sentence, keyword, skips))