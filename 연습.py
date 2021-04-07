
def func1(x):
    a, b, c = x[0], x[1], x[2]

    key =  ord(a) + ord(b) * 1000 + ord(c) * 1000000

    return key

print(func1("abc"))
print(func1("aca"))
print(func1("aca"))
print(func1("Aaa"))
print(func1("aAa"))
print(func1("aaA"))
print(func1("zzZ"))
print(func1("ZZZ"))