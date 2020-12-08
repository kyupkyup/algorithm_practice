import string


def delete_ununique_word(str1):
    table_c = {key: 0 for key in string.ascii_lowercase} # 모든 아스키코드에 해당되는 문자에 대해 0을 붙여줌
    for i in str1:
        table_c[i] += 1 # 주어진 문자열에서 각각의 문자가 몇 개인지 계산
    for key, value in table_c.items(): # 테이블의 아이템(key, value) 를
        if value > 1: # value 가 1 이상이면 중복이 있다는 뜻이므로 이 문자는 모두 제거해줘야함
            str1 = str1.replace(key, "") # 해당 문자에 대해 ""으로 치환
    return str1


def test_delete_ununique_word():
    str1= "asdfasdfahjkgk"
    result = delete_ununique_word(str1)
    print(result)
    return


if __name__ =="__main__":
    test_delete_ununique_word()
