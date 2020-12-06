
def revert(s):
    if s:
        s = s[-1] + revert(s[:-1])
    # 재귀 함수를 이용한 문자열 뒤집기
    return s


def revert2(s):
    return s[::-1]
    # 스플릿 이용한 뒤집기 ( 0부터 -1 씩 뒤에서 부터)
    # 증가폭을 마이너스로 지정했을 경우 시작 인덱스를 끝 보다 크게 지정해야함.

if __name__ == "__main__":
    str1 = "안녕 세상!"
    str2 = revert(str1)
    str3 = revert2(str1)
    print(str2)
    print(str3)
