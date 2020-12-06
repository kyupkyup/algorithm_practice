# 숫자를 base 진법으로 변환
def convert_from_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % base * multiplier # 10진법 숫자에 바꾸려는 진법 숫자의 나머지를 구함, 현재 자리수 곱셈
        multiplier *= 10 # 자리수 추가
        number = number // base #
    return result

def test_convert_from_decimal():
    number, base = 9, 2
    assert(convert_from_decimal(number, base) == 1001)
    print("통과")

test_convert_from_decimal()