"""

반복 가능, 가변객체, 중복이 없음, 정렬 없음
인덱스 연산 불가

set의 삽입 시간 복잡도 - O(n)  - 정렬이 없으므로 그냥 삽입만 하면됨

합집합의 시간복잡도 - O(m + n)
교집합의 시간복잡도 - O(n)

"""

people = {"1", "2", "3", "4"}
people.add("5")

"""
update()  합집합
union() 마찬가지로 합집합이지만 연산결과를 복사본으로 반환
"""
people.update({"1","3","10"})
print(people)

new_people = people.union({"111"})
print(new_people, people)

"""
intersection() 
교집합의 복사본 반환
"""
hi = {1,2,3,4}
hello = {2,3,4,5}
answer = hi.intersection(hello)
print(answer)

"""
difference()
A.difference(B)
A와 B의 차집합의 복사본 반환
"""






