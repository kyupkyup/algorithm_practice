

def reversing_words_sentence_logic(new_list):
    # 전체 뒤집기

    list1 = new_list[::-1]
    # 단어만 다시 뒤집기

    list2 = list1.split(" ")
    str = ""
    for i in list2:
        str += i[::-1] + " "

    print(str)

    return 0


if __name__ == "__main__":
    str1 = "파이썬 알고리즘 정말 ㅈ같다."
    str2 = reversing_words_sentence_logic(str1)