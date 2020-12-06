
"""
문자열 메소드 join
A.join(B) = B에 있는 문자열을 A로 결 합

"""
slayer = ["버피", "앤", "아스틴"]
mew2 = " j".join(slayer)

"""
문자열 메소드 ljust, rjust(width, fillchar)
ljust 는 왼쪽부터 문자열을 포함한 width 의 개수만큼 fillchar 로 채움
rjust 는 오른쪽
"""
name = "하이"
newName = name.ljust(30, "-")
print(newName)

"""
format()

"""

"""
split(t, n)
t 를 기준으로 n번만큼 분리 n 파라미터가 없으면 할 수 있는 만큼 모두 분리
"""

"""
wapcase()
문자열의 대소문자 반전 복사본 반환
"""

