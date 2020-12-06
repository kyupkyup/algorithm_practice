def convert_to_up(number, base):
    strings = "0123456789ABCDEFGHIJ"
    result = ""
    while number > 0:
        digit = number % base
        result = strings[digit] + result
        number = number // 16
    return result

def test_convert_to_up():
    number, base = 31, 16
    assert(convert_to_up(number, base) == "1F")
    print("통과")

test_convert_to_up()