# 문자열 : 불변객체
# 튜플 : 불변객체
# 리스트 : 가변
# 바이트 배열
# 바이트 : 가변객체
"""
리스트 깊은 복사 법
"""

myList = [1,2,3,4]

newList = myList[:]

newList2 = list(newList)

"""
튜플 깊은 복사
"""

people = {"버피", "에인절", "자일스"}
slayers = people # 얇은 복사
#깊은 복사를 하려면 copy()를 써야함

slayers.discard("버피")
print(slayers)
print(people)


"""
깊은 복사는 값을 모두 복사해 새로운 객체에 넣는 것.
얇은 복사는 객체의 주소를 복사하는 것
"""

hello = "asdf"

hello[1] = "asdfadsf"

print(hello)