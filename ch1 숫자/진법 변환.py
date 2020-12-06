def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier # 10을 나눈 나머지에 현재 자리수를 곱해 더한다.
        multiplier *= base # 자리수를 올려준다
        number = number // 10 # number는 10씩 나눠서 계속 다음수에 적용
    return result


def test_convert_to_decimal():
    number, base = 10010, 2
    assert (convert_to_decimal(number, base) == 18)
    print("통과")

test_convert_to_decimal()
