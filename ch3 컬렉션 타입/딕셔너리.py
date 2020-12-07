
"""
파이썬 딕셔너리 = 해시테이블

특정 객체에 해당하는 임의의 정수값을 상수 시간 내에 계산

-> 해시 충돌에 대한 공부가 필요
"""
tarantino = {}
tarantino["name"] = "쿠엔틴 타란티노"
tarantino["job"] = "감독"
print(tarantino)

sunnydale = dict({"name" : 123, "age": 12, "hobby" : 145})
print(sunnydale)


"""
setDefault()
키의 존재여부를 모른 채 접근할 때 사용
key 가 존재하면 값을 얻어오고 존재하지 않으면 새 키와 값으로 추가

update()
A.update(B) : 딕셔너리 A에 B의 키가 존재하면 갱신
없으면 추가

get()
A.get(key) A에서 key 의 value를 얻음.
"""

"""
딕셔너리 sorted
keys(), values(), items() 에 대해 사용가능

"""
d = dict(c=":!", b="world", a = "hello")
for key in sorted(d.values()):
    print(key, d.setdefault(key))
print(d)

""" 
카운터 


"""