
table =["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages=["JAVA", "JAVASCRIPT"]
preference=[7, 5]

def solution(table, languages, preference):
    answer = ''
    temp_ans = 0
    ans = []
    for row in table:
        row = row.split(" ")
        for language_index in range(len(languages)):
            for i in range(len(row)):
                if languages[language_index] == row[i]:
                    temp_ans += (preference[language_index] * (len(row) - i))
        ans.append(temp_ans)
        temp_ans = 0
    max_arr = max(ans)
    ans1 = []
    for i in range(len(table)):
        if ans[i] == max_arr:
            ans1.append(i)
    print(ans1)
    ans2 = []
    for i in ans1:
        ans2.append(table[i].split(" ")[0])
    return sorted(ans2)[0]


    # return table[index1].split(" ")[0]
print(solution(table, languages, preference))