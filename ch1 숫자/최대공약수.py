def finding_gcd(a, b):
    while b!=0:
        result = b
        a, b = b, a % b
    return result

def test_finding_gcd():
    num1, num2 = 21, 12
    assert(finding_gcd(num1, num2)== 3)
    print("통과")

test_finding_gcd()